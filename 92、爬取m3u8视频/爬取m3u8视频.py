# 爬取m3u8视频

import os 
import pprint
import re 
import time
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

## 获取m3u8列表文件

def get_m3u8_list(url):
    r = requests.get(url,headers=headers)
    # print(r.text)
    info = re.findall(r'window.pageInfo = window.videoInfo = (.*?) window.videoResource',r.text,re.S)[0].strip()[:-1]
    # info_json = json.loads(info)['currentVideoInfo']['ksPlayJson']
    info_json = json.loads(json.loads(info)['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][1]['url']
    file_name = json.loads(info)['title']
    # print(file_name)
    # pprint.pprint(info_json)
    return info_json,file_name

## 提取所有视频片段的播放地址
def get_ts_files(url):
    r = requests.get(url,headers=headers)
    # print(r.text)
    ts_files = re.sub('#.*','',r.text).split()
    # print(ts_files)
    return ts_files
    
## 下载合并视频片段
def download_combine(ts_files,video_url,video_path,file_name):
    # print(repr(file_name)) # '【国庆】请去普洱玩吧！'
    # 检查标题非法字符
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        file_name = file_name.replace(char, '_')

    # 创建目录
    directory = os.path.join(video_path, file_name)
    if not os.path.exists(directory):
        os.makedirs(directory)    
    
    # 创建视频文件路径
    video_file_path = os.path.join(directory, f'{file_name}.mp4')

    with open(video_file_path,'ab') as f:
        for ts in tqdm(ts_files):
            ts = video_url + ts
            try:
                ts_content = requests.get(ts, headers=headers).content
                f.write(ts_content)
            except Exception as e:
                print(f"下载失败: {ts}, 错误: {e}")

## 获取目录页的视频链接
def get_index_links(index_url):
    
    r =requests.get(index_url,headers=headers)
    # print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    link_list = soup.findAll('h1',class_='list-content-title')
    # print(link_list)
    links = []
    for a in link_list:
        link = 'https://www.acfun.cn' + a.a.get('href')
        # print(link)
        links.append(link)
    return links
    
def main():
    index_url = 'https://www.acfun.cn/v/list204/index.htm'
    video_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/'
    video_path = r'D:\Code\DarkCatPython\WebCrawler\爬取m3u8视频\video'
    links = get_index_links(index_url)
    for url in links:
        # url = 'https://www.acfun.cn/v/ac46330277'
        m3u8_url,file_name = get_m3u8_list(url)
        ts_files = get_ts_files(m3u8_url)
        download_combine(ts_files,video_url,video_path,file_name)
        
if __name__ == '__main__':
    main()




