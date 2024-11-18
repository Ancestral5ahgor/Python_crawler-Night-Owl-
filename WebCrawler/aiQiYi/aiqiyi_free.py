import requests
import re
from lxml import etree


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "referer": "https://www.baidu.com/link?url=JLOy-fsI41xY_jzUIFgDc___WCegj9YPBT3RbUADBIe&wd=&eqid=a5606f6d01319120000000066707e2de",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}

url = "https://www.iqiyi.com/"

r = requests.get(url, headers=headers)
print(r.status_code)
print(r.text)

# 请求网址
# https://mesh.if.iqiyi.com/tvg/lw/video_metadata?videoIds=2108593203574300&deviceId=8f415a0eb902fbd4b2823ba44e56c245&authCookie=&appVersion=12.94.20141&timestamp=1728570515721&src=pca_tvg&sign=F9F61CC3B51E9CEBE0B90AF7713F3AC2
#
