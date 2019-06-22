import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs


# 把所有链接生成出来
def get_page_urls():
    base_url = 'https://bank.cngold.org/yhwd/list_city_224_0_'

    page_websites = []
    page_count = 79
  
    for i in range(page_count):
        if i == 0:
            url = base_url+'0.html'
        else:
            num = i+1
            url = base_url+str(num)+'.html'
            
        page_websites.append(url)
        # print(url);
    return page_websites


# 获取一页的数据
def getPageData(url):
    print(url)
    doc = pq(requests.get(url).text)
    banks = []
    
    bankLis = doc('.list_wangdian>ul>li').items()
    for bankLi in bankLis:
        bank = {}
        bank['title'] = bankLi.find('.divtit>h3 a').attr('title')
        bank['phone'] = bankLi.find('.divtit .fr span').text().strip();
        bank['address'] = bankLi.find('.divcon>p>span').text().strip();
        banks.append(bank)
    return banks

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('bank.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话'])
    for bank in bankData:
        writer.writerow([bank['title'], bank['address'], bank['phone']])
    f.close()
                  
    

def init():
    page_websites = get_page_urls();
    bankData = [];
    first = page_websites[0];
    for url in page_websites:
        pageData = getPageData(url)
        bankData += pageData
        time.sleep(1+random.randint(1,50)/100)
    toFile(bankData)
    
    # toFile(getPageData(first))

init()


