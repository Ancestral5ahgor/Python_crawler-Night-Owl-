# 爬虫实战-爬取红袖添香小说

import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from lxml import etree


service = Service('E:\zsfile\pycode\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True)
opt.add_argument('--disable-blink-features=AutomationControlled')



def get_content(url):

    browser = webdriver.Chrome(service=service,options=opt)

    browser.get(url)
    page_text = browser.page_source
    # print(page_text)
    browser.close()

    html = etree.HTML(page_text)
    content = html.xpath('//div[@class="ywskythunderfont"]//text()')
    content = ''.join(content).replace('\u3000\u3000','\n\n').strip()
    # print(content)
    # return content
    # 使用正则表达式过滤掉不需要的内容
    filtered_content = re.sub(r'window\..*?;', '', content)

    return filtered_content.strip()

def get_catalog(index_url,path):
    browser = webdriver.Chrome(service=service,options=opt)
    browser.get(index_url)
    
    # //*[@id="j-catalogWrap"]/div[2]/div/ul/li[1]/a
    # //*[@id="j-catalogWrap"]/div[2]/div/ul/li[27]/a
    page_text = browser.page_source
    browser.close()
    html = etree.HTML(page_text)
    links = html.xpath('//*[@id="j-catalogWrap"]/div[2]/div/ul/li/a/@href')
    titles = html.xpath('//*[@id="j-catalogWrap"]/div[2]/div/ul/li/a/text()')
    book_name = html.xpath('/html/body/div[1]/div[2]/div[4]/div[1]/div[2]/div/h1/text()')[0]

    f = open(f'{path}/{book_name}.txt','a',encoding='utf-8')
    print(book_name)
    for link,title in zip(links,titles):
        link_url = 'https://www.hongxiu.com'+ link
        content = get_content(link_url)
        f.write(title+'\n\n')
        f.write(content+'\n\n')
        f.write('---'*40+'\n\n')
        print(f'已下载{book_name}')
    f.close()    
    


if __name__ == '__main__':
    path = r'E:\zsfile\pycode\pycode\NightCatPython'

    url ='https://www.hongxiu.com/chapter/23319469809201404/62605168155360995'

    index_url = 'https://www.hongxiu.com/book/23319469809201404#Catalog'

    get_catalog(index_url,path)

    # content = get_content(url)
    # print(content)

