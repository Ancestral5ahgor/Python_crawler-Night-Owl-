# 动态网页爬虫-处理图片验证码-
## 案例：模拟登录超级鹰

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chaojiying import Chaojiying_Client
from hashlib import md5
import json

service = Service('D:\Code\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True)
opt.add_argument('--disable-blink-features=AutomationControlled')

def login(url,username,password,soft_id):
    browser = webdriver.Chrome(service=service,options=opt)
    browser.get(url)
    browser.maximize_window()

    # 输入用户名
    time.sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(username)

    # 输入密码
    time.sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)

    # 获取验证码图片
    img = browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
    chaojiying = Chaojiying_Client(username,password,soft_id)
    code = chaojiying.PostPic(img,1902)['pic_str']
    
    # 输入验证码
    time.sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code)

    # 点击登录
    browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

if __name__ == '__main__':
    url = 'https://www.chaojiying.com/'
    with open('D:\Code\DarkCatPython\chaojiying_Python\password.json', 'r',encoding='utf-8') as f:
        info = json.loads(f.read())
    username = info['username']
    password = info['password']
    soft_id = info['soft_id']
    login(url,username,password,soft_id)
