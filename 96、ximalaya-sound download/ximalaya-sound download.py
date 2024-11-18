# 下载喜马拉雅音频

import requests
import re
import execjs
import os
import time

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'referer':'https://www.ximalaya.com/album/34220825',
    'host':'www.ximalaya.com',
    'Cookie':"_xmLog=h5&ef97dc28-3df2-4ee6-b5ad-3b45aaeb0158&process.env.sdkVersion; wfp=ACNkNmI4NTcyMGFkNjQ0ZGIzQh4jM0OwQKN4bXdlYl93d3c; 1&remember_me=y; 1&_token=53229940&1E3955E0140N12D6E1879AF823BDFB860C9E28DAE36526ABD9E8F8D993934EB944BCB1E39B6741MF885BFBCAA5BDFF_; DATE=1728177446700; crystal=U2FsdGVkX19cU84ExNEuHls4hqqz6vqSQ9aF0SU73IxfSgJhNgKwVFl19GyQZCcF8sgSsz4Ouvuzm12DaVxGWS8Nn0VAWEtM22ZaZ/MbqyVwl0S9XmXc6Tqef7s0eiWA+YtfEVLTSHlq+IJY81/PUl8XY+Hp3GtWmsg6EHSozjZnnMhXTzWlk/rs9IGb3A8oakDYV29GAj3ud5GTZmPoDbzbLoiXyggEYijQrcOM879cMHbekk5m6T4I5ME+Iu7T; xm-page-viewid=ximalaya-web; impl=www.ximalaya.com.login; Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1728177483,1728213846; HMACCOUNT=08DA46B64C34D259; Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070=1728213898; cmci9xde=U2FsdGVkX19puolDyo6xEEPwIoTyLbq9g0l49RcLrm8wfjXjkPwTkUXFW5wFwuF0t4ue+CRGoFUR491fJVzmFg==; pmck9xge=U2FsdGVkX1+fqzvELzGWGcgiKR1m3W7JdSaVyqwyHx0=; assva6=U2FsdGVkX1+1rO4gMOXlWQ7qeDRWGUtu6GHONmdIPBI=; assva5=U2FsdGVkX1+1g0lXSX1XQp4I8CmV1IiLkAGBQseIRrwPlm7kIuDTB42ynfM6DzuwdumMEpbcZD8fG+0wIgAYHw==; vmce9xdq=U2FsdGVkX188BU4Wu+ngp0FYE7FpSCPQLyxobY3z3RN4WXpRnNgtRZOmMFM9y45F3FQilRLsykcYWXiHxz9DATaX9flYffWIgOW4lH1R/RzLmwsj78nWmCTq/z9h+kbhhL5taPhYuSZmsOOOkdjV8z4M/vxiljsSIkXz6pNJ5a8=; web_login=1728213948135"
}

file_path = r'D:\Code\DarkCatPython\WebCrawler'


# 批量获取单个播放网址
link = 'https://www.ximalaya.com/revision/album/v1/getTracksList?albumId=34220825&pageNum=2&sort=0&pageSize=30'

# 发送请求，获取数据
link_json = requests.get(link,headers=headers).json()

# 提取数据
tracks = link_json['data']['tracks']
for track in tracks:
    trackId = track['trackId']

    date_time = int(time.time()*1000)
    # 单个网址
    url = f'https://www.ximalaya.com/mobile-playpage/track/v3/baseInfo/{date_time}?device=www2&trackId={trackId}&trackQualityLevel=1'

    response = requests.get(url,headers=headers)
    # print(response.status_code)
    json_data = response.json()
    # print(json_data)
    title = json_data['trackInfo']['title']
    # 替换字符
    new_title = re.sub(r'[\/:*?"<>|]+', '', title).strip()
    Mw = json_data['trackInfo']['playUrlList'][0]['url']
    # print(title,Mw)

    # 解密
    js_file = open(r'WebCrawler\ximalaya-sound download\ximalaya.js', encoding='utf-8').read()
    # 编译js代码
    js_code = execjs.compile(js_file)
    # 调用js代码函数
    e = {
        "deviceType": "www2",
        "link":Mw
    }

    play_url = js_code.call('getSoundCryptLink',e)
    print(play_url)

    ## 保存数据
    audio = requests.get(url = play_url)
    if audio.status_code != 200:
        print(f"Error: {audio.status_code}")
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    if len(audio.content) > 0:
        with open(f'{file_path}/{new_title}.m4a', 'wb') as f:
            f.write(audio.content)
    else:
        print("Received empty content.")




