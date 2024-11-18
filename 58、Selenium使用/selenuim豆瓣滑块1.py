# selenuim豆瓣滑块模拟登陆

import time
import re
import pyautogui
import urllib
import cv2
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# 引入隐式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from random import uniform


def press_button(pic_addr):
    
    loc = pyautogui.locateOnScreen(pic_addr,confidence=0.4)
    # print(loc)
    p = pyautogui.center(loc)
    pyautogui.moveTo(p)
    pyautogui.click()
    
# 封装的计算图片距离的算法
def get_pos(imageSrc):
    # 读取图像文件并返回一个image数组表示的图像对象
    image = cv2.imread(imageSrc)
    # GaussianBlur方法进行图像模糊化/降噪操作。
    # 它基于高斯函数（也称为正态分布）创建一个卷积核（或称为滤波器），该卷积核应用于图像上的每个像素点。
    blurred = cv2.GaussianBlur(image, (5, 5), 0, 0)
    # Canny方法进行图像边缘检测
    # image: 输入的单通道灰度图像。
    # threshold1: 第一个阈值，用于边缘链接。一般设置为较小的值。
    # threshold2: 第二个阈值，用于边缘链接和强边缘的筛选。一般设置为较大的值
    canny = cv2.Canny(blurred, 0, 100)  # 轮廓
    # findContours方法用于检测图像中的轮廓,并返回一个包含所有检测到轮廓的列表。
    # contours(可选): 输出的轮廓列表。每个轮廓都表示为一个点集。
    # hierarchy(可选): 输出的轮廓层次结构信息。它描述了轮廓之间的关系，例如父子关系等。
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 遍历检测到的所有轮廓的列表
    for contour in contours:
        # contourArea方法用于计算轮廓的面积
        area = cv2.contourArea(contour)
        # arcLength方法用于计算轮廓的周长或弧长
        length = cv2.arcLength(contour, True)
        # 如果检测区域面积在5025-7225之间，周长在300-380之间，则是目标区域
        if 5025 < area < 7225 and 300 < length < 380:
            # 计算轮廓的边界矩形，得到坐标和宽高
            # x, y: 边界矩形左上角点的坐标。
            # w, h: 边界矩形的宽度和高度。
            x, y, w, h = cv2.boundingRect(contour)
            print("计算出目标区域的坐标及宽高：", x, y, w, h)
            # 在目标区域上画一个红框看看效果
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imwrite("111.jpg", image)
            return x
    return 0   
    



def login(url,username,password,save_path):
    service = Service('E:\zsfile\pycode\chromedriver-win64\chromedriver.exe')
    opt = Options()
    opt.debugger_address = '127.0.0.1:8888'
    browser = webdriver.Chrome(service=service,options=opt)
    browser.get(url)
    browser.implicitly_wait(4)


    # 点击密码登陆
    #路径  //*[@id="anony-reg-new"]/div/div[1]/iframe
    
    # iframe = browser.find_element(By.XPATH,'//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
    # browser.switch_to.frame(iframe)
    time.sleep(3)
    
    browser.find_element(By.XPATH,'//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
    time.sleep(uniform(1,4))
    # 输入账号密码
    browser.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
    time.sleep(uniform(1,4))
    browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    time.sleep(uniform(1,4))
    
    # 点击登陆按钮
    # /html/body/div[1]/div[1]/ul[1]/li[2]
    pic_addr = r'E:\zsfile\pycode\pycode\NightCatPython\pic\douban-button.png'
    press_button(pic_addr)

    # 隐式等待
    # browser.webdriverwait(driver,)
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located((By.ID, "tcaptcha_iframe_dy")))

    # 切换到滑块窗口
    # 路径：//*[@id="anony-reg-new"]/div/div[1]/iframe
    iframe1 = browser.find_element(By.ID,'tcaptcha_iframe_dy')
    browser.switch_to.frame(iframe1)
    time.sleep(uniform(1,4))

    
    # 获取滑块验证图片下载路径，并下载到本地
    background_img = browser.find_element(By.ID, 'slideBg')
    s = background_img.get_attribute("style")
    # 设置能匹配出图片路径的正则表达式
    p = 'background-image: url\(\"(.*?)\"\);'
    # 进行正则表达式匹配，找出匹配的字符串并截取出来
    bigImageSrc = re.findall(p, s, re.S)[0]   # re.S表示点号匹配任意字符，包括换行符
    print(f'图片路径：{bigImageSrc}')

    file_path = save_path + '\\' + 'bigImageSrc.png'
    # 下载图片到本地
    urllib.request.urlretrieve(bigImageSrc,file_path)

    dis = get_pos(file_path)
    time.sleep(5)

    small_img = browser.find_element(By.XPATH, '//*[@id="tcOperation"]/div[6]')

    # 小滑块到目标区域的移动距离（缺口坐标的水平位置距离小滑块的水平坐标相减的差）
    # 新缺口坐标=原缺口坐标*新画布宽度/原画布宽度
    newDis = int(dis*340/672-small_img.location['x'])
    browser.implicitly_wait(3)  # 使用浏览器隐式等待5秒

    
    # 按下小滑块按钮不动
    ActionChains(browser).click_and_hold(small_img).perform()
    # 移动小滑块，模拟人的操作，一次次移动一点点
    i = 0
    moved = 0

    while moved < newDis:
        x = random.randint(3, 10)  # 每次移动3到10像素
        moved += x
        ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
        print("第{}次移动后，位置为{}".format(i, small_img.location['x']))
        i += 1

    
    # 移动完之后，松开鼠标
    ActionChains(browser).release().perform()
    # 整体等待5秒看结果
    time.sleep(4)




if __name__ == '__main__':
    url = 'https://accounts.douban.com/passport/login'
    save_path = r'E:\zsfile\pycode\pycode\NightCatPython\pic'
    
    username = '18600290000'
    password = 'sefadfwef'
    login(url,username,password,save_path)
    



