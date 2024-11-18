# 动态网页爬虫-Selenuim：切换表单frame
## 模拟登陆豆瓣网

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service('E:\zsfile\pycode\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True)
opt.add_argument('--disable-blink-features=AutomationControlled')

url = 'https://www.douban.com/'
browser = webdriver.Chrome(service=service,options=opt)
browser.implicitly_wait(4)
browser.get(url)

browser.maximize_window()
# xpath:/html/body/div[1]/div[1]/ul[1]/li[2]
time.sleep(3)
# ifram表单路径：//*[@id="anony-reg-new"]/div/div[1]/iframe
iframe = browser.find_element(By.XPATH,'//*[@id="anony-reg-new"]/div/div[1]/iframe')
browser.switch_to.frame(iframe)
browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/ul[1]/li[2]').click()

time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="username"]').send_keys('12654359756')
time.sleep(3)
browser.find_element(By.XPATH,'//*[@id="password"]').send_keys('fdsaf')
time.sleep(3)

browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[5]/a').click()

time.sleep(3)
browser.close()





