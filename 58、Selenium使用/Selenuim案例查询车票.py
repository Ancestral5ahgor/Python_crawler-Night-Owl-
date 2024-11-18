# 动态网页爬虫-Selenuim：查询车票
## 什么是动作链 ？
## selenium提供了一个类处理这类事件，这个类就是ActionChains
## 常用方法
### move_to_element():将鼠标移动指定的element，参数为标签
### move_by_offset(xoffset,yoffset):将鼠标移动到指定的偏移量，参数为x,y
### click():点击
### scroll_to_element():滚动到指定的element，参数为标签
### scroll_by_amount(x,y):鼠标滚轮安装偏移量滚动，参数为x,y
### perform():执行动作链
### context_click():右键点击
### click_and_hold(element):点击且不松开鼠标
### double_click():双击
### drag_and_drop(source,target):拖拽
### drag_and_drop_by_offset(source,xoffset,yoffset):拖拽到指定偏移量
### release(on_element=None):释放鼠标
### key_down(value,element=None):按下某个键
### key_up(value,element=None):松开某个键

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


service = Service('E:\zsfile\pycode\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True) # 防止自动推出
opt.add_experimental_option('excludeSwitches', ['enable-automation']) #隐藏自动化浏览器标识
opt.add_argument('--disable-blink-features=AutomationControlled') # 隐藏浏览器痕迹

url = 'https://www.12306.cn/index/index.html'
browser = webdriver.Chrome(service=service,options=opt)
browser.implicitly_wait(5)
browser.maximize_window()
browser.get(url)

# 把鼠标悬停在车票上
ticket_element = browser.find_element(By.XPATH,'//*[@id="J-chepiao"]/a') # 车票元素
ActionChains(browser).move_to_element(ticket_element).perform()

# 点击单程进入下一个页面
one_way_element = browser.find_element(By.XPATH,'//*[@id="megamenu-3"]/div[1]/ul/li[1]/a') # 单程元素
ActionChains(browser).click(one_way_element).perform()

# 处理弹窗，先网页无，略过
time.sleep(3)
# 输入出发点
from_station = browser.find_element(By.XPATH,'//*[@id="fromStationText"]') # 出发地元素
ActionChains(browser)\
    .click(from_station)\
    .pause(1)\
    .send_keys('西安')\
    .pause(1)\
    .send_keys(Keys.ARROW_DOWN)\
    .pause(1)\
    .send_keys(Keys.ENTER)\
    .perform()

# 输入目的地
time.sleep(1)
to_station = browser.find_element(By.XPATH,'//*[@id="toStationText"]') # 目的地元素
ActionChains(browser)\
    .click(to_station)\
    .pause(1)\
    .send_keys('北京')\
    .pause(1)\
    .send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN)\
    .pause(1)\
    .send_keys(Keys.ENTER)\
    .perform()

# 选择出发时间
time.sleep(1)
date_element = browser.find_element(By.XPATH,'//*[@id="train_date"]') # 日期元素
ActionChains(browser)\
    .click(date_element)\
    .pause(1)\
    .send_keys(Keys.ARROW_RIGHT,Keys.ARROW_RIGHT)\
    .pause(1)\
    .send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE)\
    .pause(1)\
    .send_keys('2024-09-18',Keys.ENTER)\
    .perform()

# 勾选高铁/动车
time.sleep(1)
browser.find_element(By.XPATH,'//*[@value="G"]').click() # 高铁/动车元素

# 指定发车时间
time.sleep(1)
start_time_element = browser.find_element(By.XPATH,'//*[@id="cc_start_time"]') # 发车时间元素
Select(start_time_element).select_by_visible_text('12:00--18:00') # 选择发车时间


# 点击查询
browser.find_element(By.XPATH,'//*[@id="query_ticket"]').click()

browser.close()
