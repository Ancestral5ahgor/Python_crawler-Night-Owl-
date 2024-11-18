## 京东秒杀脚本

import requests
import time
import datetime
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 等待开始时间
def timing(buy_time):
    success_login = True
    while True:
        now_time = datetime.now()
        diff_time = (buy_time - now_time).seconds()
        if diff_time > 0:
            time.sleep(1)
            try:
                WebDriverWait(browser, 3).until(
                    EC.presence_of_element_located((By.ID, "order-submit"))
                )
                print(f"登录正常，当前时间为：{now_time}")

            except:
                print(f"登录异常，当前时间为：{now_time}")
                success_login = False
                break

            time.sleep(1)
            browser.refresh(randint(40, 45))
        else:
            print(f"还有{diff_time}秒开始抢购，准备下单！")
            break
    return success_login


# 抢购
def buy():
    order_url = "https://cart.jd.com/cart_index#none"
    browser.get(order_url)
    buy_time = datetime.striptime(buy_time_org, "%Y-%m-%d %H:%M:%S.%f")
    # 等待
    success_login = timing(buy_time)
    if not success_login:
        print("登录失败，请重新登录！退出主程序")
        return

    while True:
        if datetime.now() > buy_time:
            try:
                browser.find_element(By.ID, "order-submit").click()
                print(f"已下单，当前时间为：{datetime.now()}")
                break
            except:
                print(f"下单失败，当前时间为：{datetime.now()}")
                break


if __name__ == "__main__":
    service = Service("D:\Code\chromedriver-win64\chromedriver.exe")
    opt = Options()
    opt.page_load_strategy = "eager"
    opt.debugger_address = "127.0.0.1:8888"
    browser = webdriver.Chrome(service=service, options=opt)
    buy_time_org = "2024-10-11 11:21:00.8"
    buy()
