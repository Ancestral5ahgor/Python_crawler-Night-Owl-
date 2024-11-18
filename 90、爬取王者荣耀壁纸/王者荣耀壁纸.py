# 爬取王者荣耀官网英雄壁纸
## https://pvp.qq.com/web201605/herolist.shtml

import requests
from bs4 import BeautifulSoup
import re
import os
import time
from requests_html import HTMLSession


headers = {
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
## 拼接图片链接
# https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/558/558-bigskin-1.jpg
page_num = 1
hero_id = 525
hero_name = 'lubandashi'
path = 'D:\Code\DarkCatPython\WebCrawler\爬取王者荣耀壁纸\pic'
pic_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_id}/{hero_id}-bigskin-{page_num}.jpg'

def download_pic(pic_url,path,name):
    try:
        pic_content = requests.get(pic_url, headers=headers).content
        # print(pic_content)
    except Exception as e:
        print(f"无法获取图片: {e}")
        return
    # 创建文件夹
    file_path = os.path.join(path, name)
    try:
        os.makedirs(file_path, exist_ok=True)  # 创建文件夹，如果已存在则不报错
    except Exception as e:
        print(f"无法创建文件夹: {e}")
        return
    # 保存图片
    file_name = os.path.join(file_path, f'{name}.jpg')
    try:
        with open(file_name, 'wb') as f:
            f.write(pic_content)
            print(f'已保存{name}的图片')
            # 暂停
            time.sleep(0.5)
    except Exception as e:
        print(f"无法保存图片: {e}")
    
 


## 提取一个英雄图片的数量及名字
def get_hero_detail(hero_name,hero_id):
    detail_url = f'https://pvp.qq.com/web201605/herodetail/{hero_name}.shtml'
    r = requests.get(detail_url, headers=headers)
    r.encoding = r.apparent_encoding
    # print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    # body > div.wrapper > div.zk-con1.zk-con > div > div > div.pic-pf > ul
    # /html/body/div[3]/div[1]/div/div/div[2]/ul
    content  = soup.find('ul', class_='pic-pf-list pic-pf-list3').get('data-imgname')
    pic_name = re.sub(r'&\d+', '', content).split('|')
    # print(pic_name)

    ## 下载一组英雄图片
    for num, name in enumerate(pic_name):
        num += 1
        pic_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{hero_id}/{hero_id}-bigskin-{num}.jpg'
        download_pic(pic_url, path,name)


## 获取英雄ID，拼音名称，下载所有英雄的图片
def get_hero():
    hero_lsit_url = 'https://pvp.qq.com/web201605/js/herolist.json'
    r = requests.get(hero_lsit_url, headers=headers).json()
    for detail in r:
        hero_id = detail['ename']
        hero_name = detail['id_name']
        # print(hero_id,hero_name)
        get_hero_detail(hero_name, hero_id)


if __name__ == '__main__':
    get_hero()