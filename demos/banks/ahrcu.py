import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs


session = requests.Session()
theHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'www.ahrcu.com',

}



# 在这个页面上爬取url
def get_page_urls():
    base_url = 'http://www.ahrcu.com/hf/'

    res = session.get(base_url,headers=theHeaders);
    doc = pq(res.text);

    urls = []
    adoms = doc('.list_news>li a').items()
    for aDom in adoms:
        url = aDom.attr('href');
        urls.append(url)
    
    return urls;


   
  



# 获取每一页的数据
def getPageData(url):
    print(url)
    doc = pq(requests.get(url).text)
    banks = []
    
    bankLis = doc('table tr:gt(1)').items()
 
    for bankLi in bankLis:
        bank = {}
        bank['name'] = bankLi.find('td').eq(1).text().strip();
        bank['address'] = bankLi.find('td').eq(2).text().strip();
        bank['tel'] = bankLi.find('td').eq(4).text().strip();
        banks.append(bank)
        print(bank)
    return banks

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('ahrcu.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])
    for bank in bankData:
        writer.writerow([bank.get('name'), bank.get('address'), bank.get('tel'),'',''])
    f.close()
                  
    

def init():
    page_websites = get_page_urls();
    bankData = [];
    
    for url in page_websites:
        pageData = getPageData(url)
        bankData += pageData
        time.sleep(1+random.randint(1,50)/100)
    toFile(bankData)
    
    # toFile(getPageData(first))

init()


