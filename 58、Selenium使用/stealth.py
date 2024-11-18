# 对浏览器指纹进行隐藏
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# stealth.min.js下载地址
# https://github.com/requireCool/stealth.min.js

service = Service('D:\Code\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True)
# opt.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=opt,service=service)

with open('D:\Code\DarkCatPython\stealth.min.js-main\stealth.min.js', 'r', encoding='utf-8') as f:
    js = f.read()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": js})

url = 'https://bot.sannysoft.com/'
driver.get(url)
