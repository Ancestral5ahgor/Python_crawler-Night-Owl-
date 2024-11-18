import requests
import pprint
import chardet
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import subprocess  # 执行命令行的
from functools import partial  # 固定某个参数的
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


# with open(r'D:\BaiduSyncdisk\VsCode\Python\对称加密\JS_采集网案例.js', 'r', encoding='utf-8') as f:
#     js_code = f.read()

file = 'D:\BaiduSyncdisk\VsCode\Python\SymmetricEncryption\JS_Case.js'

with open(file, 'r',encoding='UTF-8') as f:
    js_code = f.read()
    f.close()

headers = {
  "accept": "text/plain, */*; q=0.01",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
  "content-length": "127",
  "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
  "origin": "https://search.bidcenter.com.cn",
  "priority": "u=1, i",
  "referer": "https://search.bidcenter.com.cn/",
  "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-site",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

data = {
  "from": "6137",
  "guid": "a182b937-550b-4c65-9576-e7b5235b768b",
  "location": "6138",
  "token": "",
  "keywords": "%e5%a4%aa%e9%98%b3%e8%83%bd"
}

reponse = requests.post('https://interface.bidcenter.com.cn/search/GetRelatedDataHandler.ashx', headers=headers, data=data)
content = reponse.text


def aes_decrypt(cipher_text_base64):
    key ='3zKzyf6eEfuDjAG3'.encode('UTF-8')
    iv = 'fyUANZ0qSNZhhNCV'.encode('UTF-8')
    cipher_text = base64.b64decode(cipher_text_base64)
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    plain_text_unpad = cipher.decrypt(cipher_text).decode('UTF-8').rstrip('\0')
    return plain_text_unpad

plain_text = aes_decrypt(content)
plain_text_dict = json.loads(plain_text)
pprint.pprint(plain_text_dict)

# print(aes_decrypt(content))

# plain_text = execjs.compile(js_code).call('get_data', content)
# exe_obj = execjs.compile(js_code)
# result = exe_obj.call('get_data', content)
# print(result)

# pprint.pprint(plain_text)
