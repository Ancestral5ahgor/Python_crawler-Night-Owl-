# selenuim豆瓣网站滑块登录

import time
import cv2
import numpy as np
import pyautogui
# 导入 CalculateDistance 类
from CalculateDistance import CalculateDistance
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import uniform
from random import randint



def press_button():
    # 读取截图和按钮图像
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    button_image = cv2.imread('D:\Code\DarkCatPython\WebCrawler\pic\/test-login.png', cv2.IMREAD_GRAYSCALE)

    # 转换截图为灰度图像
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # 使用模板匹配查找按钮位置
    result = cv2.matchTemplate(screenshot_gray, button_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.8  # 设定阈值
    if max_val >= threshold:
        button_center = (max_loc[0] + button_image.shape[1] // 2, max_loc[1] + button_image.shape[0] // 2)
        pyautogui.moveTo(button_center)
        pyautogui.click()
    else:
        print("按钮未找到")


def handle_distance(distance):
    # 将直线距离转为缓慢的轨迹
    import random
    slow_distance = []
    while sum (slow_distance) <= distance:
        slow_distance.append(random.randint(-2, 15))
    
    if sum(slow_distance) != distance:
        slow_distance.append(distance - sum(slow_distance))
    
    return slow_distance

def drag_slide(tracks,sldie_addr):
    # 拖动滑块
    loc = pyautogui.locateOnScreen(sldie_addr)
    p1 = pyautogui.center(loc)
    pyautogui.moveTo(p1)
    pyautogui.mouseDown()
    for track in tracks:
        pyautogui.move(track,uniform(-2,2),duration=0.09)
    pyautogui.mouseUp()


def login(url, username, password,path):
    service = Service(executable_path='D:\Code\chromedriver-win64\chromedriver.exe')
    opt = Options()
    opt.debugger_address = '127.0.0.1:8888'
    browser = webdriver.Chrome(service=service, options=opt)
    browser.get(url) 

    # 点击密码登录
    # 如果是iframe框架，需要切换到iframe框架
    # iframe = browser.find_element(By.XPATH, '//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]')
    # browser.switch_to.frame(iframe)
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
    time.sleep(uniform(1,4))

    # 输入用户名和密码
    # //*[@id="username"]
    browser.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    time.sleep(uniform(1,4))
    # 输入密码
    # //*[@id="password"]
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(uniform(1,4))

    # 点击登录按钮
    press_button()

    time.sleep(2)
    # browser.switch_to.window(browser.window_handles[-1]) 

    # 判断滑块页是否出现，显式等待
    WebDriverWait(browser,5).until(
        EC.visibility_of_element_located((By.ID,'tcaptcha_iframe_dy'))
    )

    # 获取滑块背景图片
    # 如有iframe框架，需要先切换到iframe框架
    slide_iframe = browser.find_element(By.ID,'tcaptcha_iframe_dy')
    browser.switch_to.frame(slide_iframe)
    background_element = browser.find_element(By.ID,'slideBg')
    background_location = background_element.location
    print(f'背景图片位置为：{background_location}')

    background_img = background_element.screenshot_as_png

    file_name = int(time.time())
    with open(f'{path}/BG-{file_name}.png', 'wb') as f:
        f.write(background_img)
        # print(f'已下载背景图片')

    # 获取滑块图片
    slide_element1 = browser.find_element(By.XPATH,'//*[@id="tcOperation"]/div[7]')
    slide_element2 = browser.find_element(By.XPATH,'//*[@id="tcOperation"]/div[8]')

    s1 = slide_element1.size
    s2 = slide_element2.size

    if s1['width'] > 100 and s1['height'] < 20:
        slide_element = slide_element2
    else:
        slide_element = slide_element1


    slide_location = slide_element.location
    print(f'滑块图片位置为：{slide_location}')
    slide_img = slide_element.screenshot_as_png

    with open(f'{path}/SD-{file_name}.png', 'wb') as f:
        f.write(slide_img)
        # print(f'已下载滑块图片')

    # 背景图片和滑块图片的地址
    bg_addr = f'{path}/BG-{file_name}.png'
    sd_addr = f'{path}/SD-{file_name}.png'

    # 计算滑块与背景图之间x轴距离
    offset_x = slide_location['x'] - background_location['x']
    print(offset_x)
    offset_y = slide_location['y'] - background_location['y']
    print(offset_y)
    

    slide_offset = CalculateDistance(bg_addr,sd_addr,offset_x,offset_y,1)
    slide_distance = slide_offset.run()
    print(slide_distance)
   
    # 计算滑块轨迹
    tracks = handle_distance(slide_distance)

    # 拖动滑块
    slide_img_addr = 'D:\Code\DarkCatPython\WebCrawler\pic\douban_slide.png'
    drag_slide(tracks,slide_img_addr)

if __name__ == '__main__':
    url = 'https://accounts.douban.com/'
    username = 'xxxxxxxxx@qq.com'
    password = '1234567'
    path = 'D:\Code\DarkCatPython\WebCrawler\pic'
    login(url,username,password,path)
    


