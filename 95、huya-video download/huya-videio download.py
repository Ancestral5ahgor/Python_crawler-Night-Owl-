# 爬取虎牙视频

import requests
import re
import os
import json
import pprint

headers = {
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}

def download(video_id,url,file_path):
    # 获取视频的播放地址
    
    parameters = {
        # 'callback': 'jQuery112406161964675456939_1728004815178',
        'videoId': video_id,
        'uid': '',
        '_': '1728004815184'
    }

    r = requests.get(url, params=parameters, headers=headers)
    # print(r.text)
    video_url = r.json()['data']['moment']['videoInfo']['definitions'][0]['url']
    video_name = r.json()['data']['moment']['title']
    # print(video_name)
    # pprint.pprint(video_url)

    dowload_path = file_path + '/' + video_name
    video_content = requests.get(video_url).content
    if not os.path.exists(dowload_path):
        os.makedirs(dowload_path)
    with open(f'{dowload_path}/{video_name}.mp4', 'wb') as f:
        f.write(video_content)
        print(f'{video_name}.mp4' + '下载完成')

def get_video_id(index_url):
    r =requests.get(index_url, headers=headers)
    # print(r.text)

    info = re.findall(f'window.HNF_GLOBAL_INIT = (.*?)</script>', r.text)[0]
    info_json = json.loads(info)['videoData']['videoDataList']['value']
    # pprint.pprint(info_json)

    vids = []
    for info in info_json:
        video_id = info['vid']
        vids.append(video_id)
        # print(video_id)
    return vids

def main():

    file_path = r'D:\Code\DarkCatPython\WebCrawler\huya-video download\video'
    url = 'https://liveapi.huya.com/moment/getMomentContent'
    index_url = 'https://www.huya.com/video/g/meijing?set_id=33'
    vids = get_video_id(index_url)

    for vid in vids:
        # video_id = '1016723584'
        download(vid,url,file_path)

if __name__ == '__main__':
    main()

