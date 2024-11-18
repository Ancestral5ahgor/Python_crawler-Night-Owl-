# 登陆1206抢票

import requests
import json
from datetime import datetime
import time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 定义参数
class GetTicket(object):

    def __init__(self):
        with open(
            r"D:\Code\DarkCatPython\WebCrawler\12306\password\password_12306.json",
            "r",
            encoding="utf-8",
        ) as f:
            user = json.load(f)
        self.username = user["username"]
        self.password = user["password"]
        self.id = user["id"]
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        # 出发日期
        self.departure_time = "2024-10-11"
        # 出发地点
        self.departure_station = "深圳北"
        # 到达地点
        self.arrival_station = "长沙南"
        # 车次
        self.train_num = "G280"
        # 开始抢票时间
        self.scheduled_time = "2024-10-09 17:23:00"
        self.scheduled_time_strip = datetime.strptime(
            self.scheduled_time, "%Y-%m-%d %H:%M:%S"
        )
        # 座位类型
        self.seat_type = "二等座"
        ticket_list = {
            "商务座": "2",
            "一等座": "3",
            "二等座": "4",
            "硬卧": "8",
            "硬座": "10",
            "无座": "11",
        }
        self.seat_type_str = ticket_list[self.seat_type]

    # 定时模块
    def timeing(self):
        flag = True
        while True:
            diff_time = (self.scheduled_time_strip - datetime.now()).seconds
            if diff_time > 60:
                print(f"当前时间{datetime.now()},距离预定时间{diff_time}秒")
                time.sleep(10)
            elif diff_time < 30:
                print(f"抢票时间不足，退出程序")
                flag = False
                break
            else:
                print(f"还有60秒开始抢票")
                break
            # print(diff_time)
        return flag

    # 模拟登陆
    def login(self):
        success_login = True
        browser.get(self.login_url)
        time.sleep(2)
        # 输入账号
        browser.find_element(By.ID, "J-userName").send_keys(self.username)
        # 输入密码
        browser.find_element(By.ID, "J-password").send_keys(self.password)
        time.sleep(1)
        # 点击登陆
        browser.find_element(By.ID, "J-login").click()
        time.sleep(0.5)

        # 短信验证
        browser.find_element(By.ID, "id_card").send_keys(self.id)
        # 点击发送验证码
        browser.find_element(By.ID, "verification_code").click()

        # 获取用户输入的验证码
        verification_code = input("请输入验证码：")

        # 输入验证码
        browser.find_element(By.ID, "code").send_keys(verification_code)
        time.sleep(1)

        # 点击确定登陆
        browser.find_element(By.ID, "sureClick").click()
        time.sleep(1)

        # 判断是否登陆成功
        try:
            WebDriverWait(browser, 4).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "welcome-con"))
            )
            print("登陆成功")
        except:
            print("登陆失败")
            success_login = False

        # 点击首页
        browser.find_element(By.XPATH, r"//*[@id='J-index']/a").click()
        time.sleep(1)

        return success_login

    # 保持登录
    def stay_login(self):
        time.sleep(1)
        # 点击用户名进入界面
        browser.find_element(By.XPATH, r"//*[@id='J-header-logout']/a[1]").click()
        time.sleep(2)

        # 如有其他窗口，点击关闭
        try:
            browser.find_element(By.CLASS_NAME, "model-close").click()
        except:
            print("没有其他窗口需要关闭")

        while True:
            # 计算距离抢票的时间
            diff_time = (self.scheduled_time_strip - datetime.now()).seconds
            if diff_time > 15:
                print("刷新用户界面，保持登录")
                browser.refresh()
                time.sleep(5)
                # 如有其他窗口，点击关闭
                try:
                    browser.find_element(By.CLASS_NAME, "model-close").click()
                except:
                    print("没有其他窗口需要关闭")
            else:
                print("距离抢票时间还有15秒，进入购票界面！")
                break

        browser.back()
        time.sleep(1.5)

        # 如有其他窗口，点击关闭
        try:
            browser.find_element(By.CLASS_NAME, "model-close").click()
        except:
            print("没有其他窗口需要关闭")

    # 查询车票
    def query_ticket(self):
        url = "https://www.12306.cn/index/"
        browser.get(url)
        time.sleep(1)

        # 输入出发地
        from_station = browser.find_element(By.ID, "fromStationText")
        from_station.send_keys(Keys.CONTROL, "a")
        from_station.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        from_station.send_keys(self.departure_station)
        time.sleep(1)
        from_station.send_keys(Keys.ENTER)

        # 输入到达地
        to_station = browser.find_element(By.ID, "toStationText")
        to_station.send_keys(Keys.CONTROL, "a")
        to_station.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        to_station.send_keys(self.arrival_station)
        time.sleep(1)
        to_station.send_keys(Keys.ENTER)

        # 输入出发日期
        train_date = browser.find_element(By.ID, "train_date")
        train_date.send_keys(Keys.CONTROL, "a")
        train_date.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        # 获取当前日期
        now_date = datetime.now().strftime("%Y-%m-%d")
        # 判断输入日期是否为过去的时间，无效时间则重新输入
        if now_date > self.departure_time:
            print("输入日期为过去时间，重新输入")
        train_date.send_keys(self.departure_time)
        time.sleep(1)
        train_date.send_keys(Keys.ENTER)

        # 勾选高铁/动车

        # 点击查询
        time.sleep(1)
        browser.find_element(By.ID, "search_one").click()

        # 切换窗口
        time.sleep(1)
        browser.switch_to.window(browser.window_handles[-1])
        try:
            close_btn = WebDriverWait(browser, 3).until(
                EC.presence_of_element_located(
                    (By.ID, "qd_closeDefaultWarningWindowDialog_id")
                )
            )
            close_btn.click()

        except:
            print("未找到关闭按钮，退出主程序！")

        time.sleep(1)
        browser.find_element(By.ID, "query_ticket").click()
        time.sleep(1)

    # 抢票
    def booking_ticket(self):
        success_flag = False
        # 点击查询按钮
        browser.find_element(By.ID, "query_ticket").click()
        # 等待数据加载
        WebDriverWait(browser, 3, 0.01).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="queryLeftTable"]/tr'))
        )
        # 获取网页源代码
        page_text = browser.page_source
        # 解析网页源代码
        html = etree.HTML(page_text)
        query_table = html.xpath('//*[@id="queryLeftTable"]/tr')
        for num in range(len(query_table) - 1):
            if num % 2 == 1:
                continue
            # 获取车次,出发站，到达站
            train_num_query = query_table[num].xpath('.//a[@class="number"]/text()')[0]
            departure_place_query = query_table[num].xpath(
                './/div[@class="cdz"]/strong[1]/text()'
            )[0]
            arrive_place_query = query_table[num].xpath(
                './/div[@class="cdz"]/strong[2]/text()'
            )[0]

            # 判断车次
            if (
                train_num_query == self.train_num
                and departure_place_query == self.departure_station
                and arrive_place_query == self.arrival_station
            ):
                print(f"找到{train_num_query}车次，开始抢票")
                ticket_left = query_table[num].xpath(
                    f".//td[{self.seat_type_str}]//text()"
                )[0]
                if ticket_left == "有" or eval(ticket_left) >= 1:
                    print(
                        f"目标车次{self.train_num}...{self.seat_type}有票，开始预定车票！"
                    )
                    # //*[@id="ticket_6i0000G83400_01_09"]/td[13]/a
                    # 点击预定按钮
                    browser.find_element(
                        By.XPATH, f'//*[@id="queryLeftTable"]/tr[{num+1}]/td[13]/a'
                    ).click()
                    print(f"已点击预定按钮，当前时间时：{datetime.now()}")

                    time.sleep(1)
                    # 等待乘车人元素加载
                    passenger_ele = WebDriverWait(browser, 3).until(
                        EC.presence_of_all_elements_located(
                            (By.ID, "normal_passenger_0")
                        )
                    )
                    passenger_ele.click()

                    # 选择座次等级
                    seat_type_ele = browser.find_element(By.ID, "seatType_1")
                    seat_type_list = {
                        "二等座": "0",
                        "一等座": "M",
                        "商务座": "9",
                        "硬卧": "3",
                        "硬座": "1",
                        "软卧": "4",
                    }
                    seat_value = seat_type_list[self.seat_type]
                    Select(seat_type_ele).select_by_value(seat_value)

                    # 提交订单
                    browser.find_element(By.ID, "submitOrder_id").click()
                    # 选择座位
                    seat_btn = WebDriverWait(browser, 6).until(
                        EC.element_to_be_clickable((By.ID, "1A"))
                    )
                    seat_btn.click()

                    # 提交确认
                    submit_btn = WebDriverWait(browser, 6).until(
                        EC.element_to_be_clickable((By.ID, "qr_submit_id"))
                    )
                    submit_btn.click()

                    success_flag = True
                else:
                    print(f"目标车次{self.train_num}无座！")

                break
        return success_flag

    # 主程序
    def run(self):
        # 等待模块
        self.timeing()
        # 模拟登录
        success_login = self.login()
        if not success_login:
            print("未登录成功，退出主程序！")
            return
        ## 查询车票
        self.query_ticket()
        # 保持登录
        self.stay_login()
        # 开始购票
        self.booking_ticket()

        max_try = 5
        try_time = 0
        while True:
            if datetime.now() > self.scheduled_time_strip:
                print(f"进入抢票，当前时间时是：{datetime.now()}")
                success_booking = self.booking_ticket()

                if success_booking:
                    print("抢票成功！请尽快付款")
                    break
                elif try_time > max_try:
                    print("抢票失败，退出主程序！")


if __name__ == "__main__":
    # "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=8888 --user-data-dir="E:\zsfile\chrome"
    service = Service("D:\Code\chromedriver-win64\chromedriver.exe")
    opt = Options()
    opt.page_load_strategy = "eager"
    opt.debugger_address = "127.0.0.1:8888"
    browser = webdriver.Chrome(service=service, options=opt)
    get_ticket = GetTicket()
    get_ticket.run()
