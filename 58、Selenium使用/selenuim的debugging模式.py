# 使用selenuim的debugging模式，让selenuim链接事先配置好的浏览器

# google浏览器安装位置
# C:\Program Files\Google\Chrome\Application

# 创建并配置一个浏览器
# chrome.exe --remote-debugging-port=8888 --user-data-dir="D:\Code\chrome"

# 快捷方式设置参数：
## 在chrome快捷方式上右击属性，目标栏后面加空格加上下面明命令：
## "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="D:\Code\chrome"

import time  # 如果后续需要使用time模块，保留此行，否则可以删除
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

service = Service('D:\Code\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.debugger_address = '127.0.0.1:8888'

browser = webdriver.Chrome(service=service, options=opt)
url = 'https://accounts.douban.com/passport/login'
browser.get(url)

# 如果需要使用time模块进行延时操作，可以这样写：
# time.sleep(5)  # 延时5秒

