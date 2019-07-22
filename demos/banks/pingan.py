import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs

import re
import json


session = requests.Session()
theHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'bank.pingan.com',

}

# 把所有链接生成出来
def get_page_urls():

  


    page_websites = ['https://ebank.pingan.com.cn/rsb/bron/coss/cust/app/getBankShowListJsonp?callback=callback&source=WEB&srhKeyword=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E5%AD%97..&city=%E5%90%88%E8%82%A5&type=YYWD&_=1563283221574']

        
    return page_websites


# 获取一页的数据
def getPageData(url):
    print(url)
    global session
    res = session.get(url,headers=theHeaders);

    text = res.text;
    # print(text)
    # callbackData =re.findall(r"callback\((.*)\)", text)[0].json();
     

    return json.loads(re.findall(r"callback\((.*)\)", text)[0]).get('data')




# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('pingan.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])

    for bank in bankData:
        writer.writerow([bank.get('name'), bank.get('address'), bank.get('tles')[0],bank.get('lng'),bank.get('lat')])
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


