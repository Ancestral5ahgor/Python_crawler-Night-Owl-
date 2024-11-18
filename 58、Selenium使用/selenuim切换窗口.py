# 动态网页爬虫，切换窗口
## 浏览器窗口切换 
## driver.switch_to.window(driver.window_handles[-1])
# 打开新的窗口
## driver.switch_to.new_window('tab')
# 打开一个新的窗口并切换至新窗口
## driver.switch_to.new_window('window')
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='D:\Code\chromedriver-win64\chromedriver.exe')
opt = Options()
opt.add_experimental_option('detach',True)
opt.page_load_strategy = 'eager'
# opt.page_load_strategy = 'eager'
# 添加以下行以跳过 SSL 证书验证
opt.add_argument('--ignore-certificate-errors')

url = 'https://club.lenovo.com.cn/forum-1219-1.html'
browser = webdriver.Chrome(service=service,options=opt)
browser.get(url)

time.sleep(3)
browser.switch_to.new_window('tab')
browser.get('https://jd.com')
time.sleep(3)
page_content = browser.page_source
print(page_content)
browser.switch_to.window(browser.window_handles[0])
# xpath路径
## //*[@class="forum_info"]/h3/a[2]
locator = (By.XPATH,'//*[@class="forum_info"]/h3/a[2]')
WebDriverWait(browser,5).until(EC.presence_of_all_elements_located(locator))


next_page = browser.find_elements(By.XPATH,'//*[@class="forum_info"]/h3/a[2]')
# 我想打印看一下next_page的内容
for next in next_page:
    browser.execute_script("arguments[0].click();",next)
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[-1])
    #//*[@id="thread_subject"]//*[@id="postlist"]/div[1]/div[1]/table/tbody/tr[1]/td/h3
    locator1 = (By.XPATH,'//*[@id="postlist"]/div[1]/div[1]/table/tbody/tr[1]/td/h3')
    WebDriverWait(browser,10).until(EC.presence_of_element_located(locator1))
    filename = browser.find_element(By.XPATH,'//*[@id="postlist"]/div[1]/div[1]/table/tbody/tr[1]/td/h3').text
    # //*[@id="postlist"]/div[1]/div[1]/table/tbody/tr[2]/td
    concent = browser.find_element(By.XPATH,'//*[@id="postlist"]/div[1]/div[1]/table/tbody/tr[2]/td').text
    filename = filename.replace(' 【', '').replace('】','')
    with open(f'D:\Code\DarkCatPython\WebCrawler\/test\{filename}.txt','w',encoding='utf-8') as f:
        f.write(filename + '\n\n')
        f.write(concent + '\n\n') 
        print(f'已下载...{filename}')
    # print(filename,concent)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
          
    # print(next.get_attribute('href'))
else:    
    print('没有对应的元素')






