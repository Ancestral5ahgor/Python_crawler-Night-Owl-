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
from random import randint, uniform  # 合并random模块的导入
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC  # 添加缺失的导入



def login(url):
    
    opt = Options()
    opt.add_argument('--disable-blink-features=AutomationControlled') # 隐藏浏览器痕迹
    service = Service('E:\zsfile\pycode\chromedriver-win64\chromedriver.exe')
    # opt.debugger_address = '127.0.0.1:8888'
    browser = webdriver.Chrome(service=service,options=opt)
    browser.get(url)
    browser.implicitly_wait(4)

    # 读取本地图片文件并上传
    with open('a.png', 'rb') as f:
        im = f.read()
    

# 读取本地cookie文件并加载
    with open(r'E:\zsfile\pycode\pycode\NightCatPython\Cooikes\cookies.json','r',encoding='utf-8') as f:
        cookies = json.loads(f.read())
        print('已读取cookies')


        for cookie in cookies:
            cookie_dict = {
                "name": cookie.get('name'),
                "value": cookie.get('value'),
                "domain": cookie.get('domain', 'www.chaojiying.com'),  # 使用实际域名
                "path": cookie.get('path', '/'),
                "expires": cookie.get('expires', ''),
                "httpOnly": cookie.get('httpOnly', False),
                "Secure": cookie.get('Secure', False)
            }
            print(f'正在添加Cookie---{cookie_dict}')
            browser.add_cookie(cookie_dict)

    time.sleep(3)
    print('已刷新过页面')
    browser.refresh()
    time.sleep(10)

    # 检测页面是否含有个人信息，验证是否登陆成功
    page_text = browser.page_source
    # print(page_text)
    if 'SoiTeoh' in page_text:
        print('登陆成功')
     
    else:
        print('登陆失败')
    browser.quit()






if __name__ == '__main__':
    url = 'https://www.chaojiying.com/'
    
    # username = 'xxxxxxxx'
    # password = 'xxxxxxxxxx'
    login(url)
    



