## 实战案例 - 爬取TX动漫

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path='D:\Code\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True) # 防止自动推出
opt.add_experimental_option('excludeSwitches', ['enable-automation']) #隐藏自动化浏览器标识
opt.add_argument('--disable-blink-features=AutomationControlled') # 隐藏浏览器痕迹
opt.headless = True

def download(url,file_path):
    browser = webdriver.Chrome(service=service,options=opt)
    browser.maximize_window()
    browser.get(url)

    time.sleep(1)
    filename = browser.find_element(By.XPATH,'//*[@id="comicTitle"]/span[@class="title-comicHeading"]').text
    pic_list = browser.find_elements(By.XPATH,'//*[@id="comicContain"]/li/img')


    for num , pic in enumerate(pic_list):
        time.sleep(0.5)
        ActionChains(browser).scroll_to_element(pic).perform()

        link = pic.get_attribute('src')
        # print(link)
        pic_content = requests.get(link).content
        if not os.path.exists(f'{file_path}/{filename}'):
            os.makedirs(f'{file_path}/{filename}')
        with open(f'{file_path}/{filename}/{num}.jpg' , 'wb') as f:
            f.write(pic_content)
            print(f'已下载。。。{filename}...{num}张')

    next_page = browser.find_element(By.XPATH,'//*[@id="mainControlNext"]').get_attribute('href')

    browser.close()
    return next_page

if  __name__ == '__main__':

    url = 'https://ac.qq.com/ComicView/index/id/651757/cid/808'
    file_path = 'D:\Code\DarkCatPython\WebCrawler\爬取TX动漫\pic'

    while url:
        url = download(url,file_path)
    