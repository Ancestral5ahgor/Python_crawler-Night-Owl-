# 反反爬 - ip代理

## 快代理

import requests
import re

api_url = ''

# 获取API接口返回的代理IP
proxy_ip = requests.get(api_url).text

# 用户名密码认证（私密代理/独享代理）
username = ''
password = ''
proxies = {
    "http":"http://%(user)s:%(pwd)s@%(proxy)s/" % {"user":username, "pwd":password, "proxy":proxy_ip},
    "https":"https://%(user)s:%(pwd)s@%(proxy)s/" % {"user":username, "pwd":password, "proxy":proxy_ip}
}

# 代理IP
proxy_ip = re.findall(r'\d+\.\d+\.\d+\.\d+:\d+', proxy_ip)[0]

# 测试代理IP
print(requests.get('http://httpbin.org/ip', proxies=proxies).text)


# 要访问的目标网页
target_url = ''

# 使用代理IP发送请求
response = requests.get(target_url, proxies=proxies)

# 获取页面内容
if response.status_code == 200:
    print(response.text)



