 # 反反爬-使用cookie

##获取cookie
### 登陆账号
### 获取cookie，下载到本地
## 使用cookie
### 打开要登录的域名
### 获取本地预存的cookie
### 加载到浏览器中，刷新

import time
import json
import urllib.request as urllib  # 修改为正确的urllib导入方式
from random import randint, uniform  # 合并random模块的导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 添加缺失的导入
from selenium.webdriver.support import expected_conditions as EC  # 添加缺失的导入
from selenium.webdriver.common.action_chains import ActionChains  # 添加缺失的导入
from chaojiying_Python.chaojiying import Chaojiying_Client


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
    
    # browser.find_element(By.XPATH,'//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
    # time.sleep(uniform(1,4))
    # 输入账号密码
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(username)
    time.sleep(uniform(1,4))
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)
    time.sleep(uniform(1,4))
    
    # 点击登陆按钮
    # /html/body/div[1]/div[1]/ul[1]/li[2]
    pic_element = browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img')
    pic_element.screenshot('a.png')  # 保存截图为图片文件  # 保存截图为图片文件

    # # 保存图片到本地
    # with open('a.jpg', 'wb') as f:
    #     f.write(image_bytes)

    # 读取本地图片文件并上传
    with open('a.png', 'rb') as f:
        im = f.read()
    

    # 使用超级鹰解析验证码
    # 创建 Chaojiying_Client 类的实例
    chaojiying = Chaojiying_Client('SoiTeoh', 'T2zwdsm@chaojiying', '963173')
    yanzhengma = chaojiying.PostPic(im, 1902)
    print(yanzhengma)

    # /html/body/div[3]/div/div[3]/div[1]/form/p[3]/input
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(yanzhengma['pic_str'])
    time.sleep(uniform(1,4))


    # /html/body/div[3]/div/div[3]/div[1]/form/p[4]/input
    # 点击登陆按钮
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
    time.sleep(1)

    # 检测页面是否含有个人信息，验证是否登陆成功
    page_text = browser.page_source
    # print(page_text)
    if 'SoiTeoh' in page_text:
        print('登陆成功')
        # 保存cookie到本地
        cookies = browser.get_cookies()
        chaojiying_cookies = json.dumps(cookies)
        with open(r'E:\zsfile\pycode\pycode\NightCatPython\Cooikes\cookies.json','w',encoding='utf-8') as f:
            f.write(chaojiying_cookies)
            print('保存cookie成功')
    else:
        print('登陆失败')
    browser.quit()






if __name__ == '__main__':
    url = 'https://www.chaojiying.com/user/login/'
    save_path = r'E:\zsfile\pycode\pycode\NightCatPython\pic'
    
    username = 'xxxxxxx'
    password = 'xxxxxxxxx'
    login(url,username,password,save_path)
    



