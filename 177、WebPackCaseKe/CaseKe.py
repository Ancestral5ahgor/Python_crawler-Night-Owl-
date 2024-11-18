from requests import Session
import pprint
import subprocess  # 执行命令行的
from functools import partial  # 固定某个参数的
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

session = Session()

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'select_city=440300; lianjia_ssid=61fa3382-e688-47bd-aeff-471f0e936fd7; lianjia_uuid=9725d9a5-0283-4d99-b00b-bc49d5c097c0; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1731914571; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1731914571; HMACCOUNT=FA6BFF3F95279EA8; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221933e271dd3ab2-0cf680d0b256f5-26011951-1474560-1933e271dd414b2%22%2C%22%24device_id%22%3A%221933e271dd3ab2-0cf680d0b256f5-26011951-1474560-1933e271dd414b2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D',
    'Origin': 'https://sz.ke.com',
    'Referer': 'https://sz.ke.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

session.options(url='https://clogin.ke.com/authentication/authenticate', headers=headers)

# print(session.cookies)
# exit()

json_data = {
    'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
    'version': '2.0',
}

response = session.post('https://clogin.ke.com/authentication/initialize', headers=headers, json=json_data)

# pprint.pprint(response.json())

loginTicketId = response.json()['loginTicketId']
publicKey = response.json()['publicKey']['key']

# print(loginTicketId,publicKey)

t = {"username":"18754987639",
     "password":"123456789as",
     "encodeVersion":"1"
     }

with open(r'D:\BaiduSyncdisk\VsCode\Python\WebPackCaseKe\beike_login.js', 'r', encoding='utf-8') as f:
    js = f.read()

password = execjs.compile(js).call('get_pwd', t, publicKey)
# print(password)


json_data = {
    'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
    'mainAuthMethodName': 'username-password',
    'accountSystem': 'customer',
    'credential': {
        'username': t['username'],
        'password': password,
        'encodeVersion': '1',
    },
    'context': {
        'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'clientSource': 'pc',
        'os': 'Windows',
        'osVersion': '10',
        'registerPosLx': 447.1000061035156,
        'registerPosLy': 413.70001220703125,
        'registerPosRx': 727.1000061035156,
        'registerPosRy': 1044.1000366210938,
        'clickPosX': 592,
        'clickPosY': 438,
        'screen': '935_774',
        'dataId': 'BbO5klwH2Y5HnLGCNjsJ1WRJFJK2tB5brtRfIFrtx6Vv0Ywj9iN6ckzyf/UNTzKQ',
    },
    'loginTicketId': loginTicketId,
    'version': '2.0',
    'srcId': 'eyJ0Ijoie1wiZGF0YVwiOlwiMjMyZWYyY2QyMmM1MjhlMmZjYThlNGE2NjJjOTJiNzI3YTU2ZTM1N2UyZGY1Y2NjY2IwOTRjN2NmNTk3ZGU4Y2M4ZDQ5MmZhY2M4Y2ViYjkyOWRjZjdhMDUxNzQ0MDU3MjA1ZDdmOGJiMDNmZGU0OGNkZjZkMWM1YTZkNWI0Mzg1NmRkM2MzNTRmMmFkOThlMjMwNmFiNTVmODU0MTMxMmIzY2M5NzNmNzkzMDliOTg5MjFhZGNlYjdjYTU4MzJlY2QzNDZlOWRhMmZlM2VmMTI1ODE5MmZhNDI0N2QxZGI4MTUwMTI0Mzc4ZmFhZmU1ZThmYzJhNTRmNGJlZWM5MlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJlZDYwNjUwNVwifSIsInIiOiJodHRwczovL3N6LmtlLmNvbS8/dXRtX3NvdXJjZT1iYWlkdSZ1dG1fbWVkaXVtPXBpbnpodWFuJnV0bV90ZXJtPWJpYW90aSZ1dG1fY29udGVudD1iaWFvdGltaWFvc2h1JnV0bV9jYW1wYWlnbj13eXNoZW56aGVuIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=',
    'ticketMaxAge': 604800,
}

response = session.post('https://clogin.ke.com/authentication/authenticate', headers=headers, json=json_data)

print(response.text)
