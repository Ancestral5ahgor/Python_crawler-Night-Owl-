import requests

from lxml import etree

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}

url = 'https://music.163.com/#/artist?id=40281'


response = requests.get(url,headers=headers)
if response.status_code == 200:
    print(response.text)
    # 解析网页
    html = etree.HTML(response.text)

    # 通过xpaht解析获取歌曲id
    song_list = html.xpath('//*[@id="201100491731737973448"]/td[2]/div/div/div/span/a/@href')
    # //*[@id="201100491731737973448"]/td[2]/div/div/div/span/a
    print(song_list)



else:
    print('请求失败')



