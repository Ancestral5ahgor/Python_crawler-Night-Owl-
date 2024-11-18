# 反反爬 - user-agnet

# 构建一个user-agent池，

from fake_useragent import UserAgent
import requests


us = UserAgent()
user_agent = us.random
# print(user_agent)


headers = {'User_agent':user_agent}

url = 'https://www.baidu.com'
r = requests.get(url,headers=headers)
print(r.text)
