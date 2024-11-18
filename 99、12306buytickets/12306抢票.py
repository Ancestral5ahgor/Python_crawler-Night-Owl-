## 12306购票
import json
import time
from datetime import datetime


class GetTicket:

    # 定义参数
    def __init__(self):
        with open(
            r"D:\Code\DarkCatPython\WebCrawler\12306\password\password_12306.json",
            "r",
            encoding="utf-8",
        ) as f:
            user = json.loads(f.read())
        self.username = user["username"]
        self.password = user["password"]
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.depature_time = "2022-01-01"

        self.depature_station = "深圳北"

        self.arrival_station = "青岛"

        self.train_num = "T398"
        # 车次
        self.schduled_time = "2024-10-10 07:21:00"
        self.schduled_time_strip = datetime.strptime(
            self.schduled_time, "%Y-%m-%d %H:%M:%S"
        )
        self.seat_type = "一等座"

    # 定时模块
    def timing(self):
        flag = True
        while True:
            # 获取当前时间
            diff_time = (self.schduled_time_strip - datetime.now()).seconds
            if diff_time > 60:
                print("距离抢票时间还有{}秒".format(diff_time))
                time.sleep(1)
            elif diff_time < 30:
                print("距离抢票时间还有{}秒,请注意".format(diff_time))
                flag = False
                break
            else:
                print("还有60秒开始，启动程序。。。")
                break
        print(datetime.now())
        pass

    # 模拟登录
    def login(self):
        pass

    # 保持登录
    def stay_login(self):
        pass

    # 抢票
    def booking_ticket(self):
        pass

    # 主程序
    def run(self):
        self.timing()


if __name__ == "__main__":
    get_ticiket = GetTicket()
    GetTicket().run()
