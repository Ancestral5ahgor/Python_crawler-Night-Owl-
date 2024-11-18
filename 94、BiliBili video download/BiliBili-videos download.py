## 爬取B站视频
import os
from lxml import etree
import requests
import re
import json
import subprocess

requests.packages.urllib3.disable_warnings()

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.bilibili.com',
}

def download_video(url,file_path,session=requests.session()):

    ## 爬取网页源代码
    response = session.get(url,headers=headers,verify=False)
    # print(response.text)

    html = etree.HTML(response.content)
    videoinforms = str(html.xpath('//head/script[4]/text()')[0])[20:]
    videojson = json.loads(videoinforms)
    # print(videojson)

    ## 提取视频和音频的播放地址
    try:
        VideoURL = videojson['data']['dash']['video'][0]['baseUrl']
        AudioURL = videojson['data']['dash']['audio'][0]['baseUrl']
        flag=0
    except Exception:
        # 2018年以前的b站视频，格式为flv
        VideoURL = videojson['data']['durl'][0]['url']
        flag=1

    file_name = html.xpath("/html/head/title/text()")[0].strip()
    # 确保 file_name 中没有非法字符
    file_name = ''.join(c for c in file_name if c.isalnum() or c in (' ', '_')).rstrip()
    # print(file_name)

    # 创建目录
    output_dir = os.path.join(file_path, file_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print('目录文件创建成功!')

    print(f'开始下载{file_name}的视频····')

    video_file_path = os.path.join(output_dir, f'{file_name}_Video.mp4')
    BiliBiliDownload(url,VideoURL, name=video_file_path, session=session)

    if flag==0:
        print(f'开始下载{file_name}的音频····')
        audio_file_path = os.path.join(output_dir, f'{file_name}_Audio.mp3')
        BiliBiliDownload(url, AudioURL, name=audio_file_path, session=session)
        print(f'开始组合{file_name}的视频和音频····')
    
        CombineVideoAudio(video_file_path, audio_file_path, os.path.join(output_dir, f'{file_name}_output.mp4'))
    
    print(f'{file_name}下载完成！')

## 下载并保存视频和音频
def BiliBiliDownload(url, URL, name, session=requests.session()):
    headers.update({'Referer': url})
    session.options(url=URL, headers=headers,verify=False)
    # 每次下载1M的数据
    begin = 0
    end = 1024*512-1
    flag=0
    while True:
        headers.update({'Range': 'bytes='+str(begin) + '-' + str(end)})
        res = session.get(url=URL, headers=headers,verify=False)
        if res.status_code != 416:
            begin = end + 1
            end = end + 1024*512
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = session.get(url=URL, headers=headers,verify=False)
            flag=1
        with open(name, 'ab') as fp:
            fp.write(res.content)
            fp.flush()

        # data=data+res.content
        if flag==1:
            fp.close()
            break
    
## 合并视频和音频
def CombineVideoAudio(video_file_path,audio_file_path,output_dir):
    # 构建 ffmpeg 命令
    command = [
        'ffmpeg',
        '-i', video_file_path,   # 输入视频文件
        '-i', audio_file_path,   # 输入音频文件
        '-c:v', 'copy',    # 视频流复制
        '-c:a', 'aac',     # 设置音频编码
        '-strict', 'experimental',
        output_dir            # 输出文件
    ]

    # 调用 ffmpeg
    subprocess.run(command)

    # 删除临时文件（可选）
    # os.remove(video_file_path)
    # os.remove(audio_file_path)

def main():
    
    file_path = r'D:\Code\DarkCatPython\WebCrawler\爬取B站视频\video'
    for i in range(177,178):
        url = f"https://www.bilibili.com/video/BV1PZvCe2E9A/?p={i}&vd_source=1060dcfd4d6fb61eabf0fed0e994f4bf"
        print(url)
        download_video(url,file_path)
        
if __name__ == '__main__':
    main()



