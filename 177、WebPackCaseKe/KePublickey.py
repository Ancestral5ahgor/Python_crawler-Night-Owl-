import requests
import pprint

cookies = {
    'select_city': '440300',
    'lianjia_ssid': '61fa3382-e688-47bd-aeff-471f0e936fd7',
    'lianjia_uuid': '9725d9a5-0283-4d99-b00b-bc49d5c097c0',
    'Hm_lvt_b160d5571570fd63c347b9d4ab5ca610': '1731914571',
    'Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610': '1731914571',
    'HMACCOUNT': 'FA6BFF3F95279EA8',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221933e271dd3ab2-0cf680d0b256f5-26011951-1474560-1933e271dd414b2%22%2C%22%24device_id%22%3A%221933e271dd3ab2-0cf680d0b256f5-26011951-1474560-1933e271dd414b2%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyshenzhen%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D',
}

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

json_data = {
    'service': 'https://ajax.api.ke.com/login/login/getuserinfo',
    'version': '2.0',
}

response = requests.post('https://clogin.ke.com/authentication/initialize', cookies=cookies, headers=headers, json=json_data)

pprint.pprint(response.json())

loginTicketId = response.json()['loginTicketId']
publicKey = response.json()['publicKey']['key']



