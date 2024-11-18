# 实战案例：爬取飞卢小说

import requests
import re
import time
from bs4 import BeautifulSoup
import urllib3

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'

}

# 获取小说页的网页源代码
url = 'https://b.faloo.com/1217177_1.html'

def get_content(url):
    r = requests.get(url,headers=headers, verify=False)
    # print(r.text)

    # 提取小说文字部分内容
    soup = BeautifulSoup(r.text,'html.parser')
    # print(soup.prettify())
    content = soup.find('div',class_='noveContent').text
    # content = content.replace('【恭喜宿主.*|中秋佳节.*|立即抢充.*','',content)
    content = re.sub('【恭喜宿主.*|中秋读书.*|立即抢充.*', '',content).strip()

    # print(content)
    return content

# 获取目录页网页源代码



# 提起所有章节的链接和标题
def get_links(index_url):

    r = requests.get(index_url,headers=headers, verify=False)
    # print(r.text)

    soup = BeautifulSoup(r.text,'html.parser')
    infos = soup.find_all('div',class_="DivTd3")
    links = []
    titles = []
    for info in infos:
        title = info.find('a').text
        link = info.find('a')['href']
        url = 'https:' + link
        links.append(url)
        titles.append(title)
        # print(title,url)
    filename = soup.find('div',class_="TitleDiv muluh2").text.strip()
    # print(filename)

    return filename,links,titles

# 下载并保存所有章节小说
def download(link,title,filename,path):
    content = get_content(link)
    with open(f'{path}/{filename}.txt','a',encoding='utf-8') as f:
            f.write(title + '\n\n')
            f.write(content + '\n\n')
            f.write('--'*40 + '\n\n')
            print('已下载',title)
            time.sleep(1)

if __name__ == '__main__':
    index_url = 'https://b.faloo.com/1217177.html'
    path = 'D:\Code\DarkCatPython\WebCrawler\爬取卢某小说'
    filename,links,titles = get_links(index_url)
    for link,title in zip(links,titles):
        download(link,title,filename,path)
        
        
