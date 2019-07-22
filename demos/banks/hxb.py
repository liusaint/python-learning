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
    'Host': 'www.hxb.com.cn',

}

# 把所有链接生成出来
def get_page_urls():

  


    page_websites = ['http://www.hxb.com.cn/hxmap/get_bank.jsp?jsonpcallback=callback&params.proNo=ANH&params.branchCode=340100&params.bankName=&params.bankType=1&page=1&params.status=1&_=1563286964839','http://www.hxb.com.cn/hxmap/get_bank.jsp?jsonpcallback=callback&params.proNo=ANH&params.branchCode=340100&params.bankName=&params.bankType=1&page=2&params.status=1&_=1563286964839','http://www.hxb.com.cn/hxmap/get_bank.jsp?jsonpcallback=callback&params.proNo=ANH&params.branchCode=340100&params.bankName=&params.bankType=0&page=1&params.status=1&_=1563286964843','http://www.hxb.com.cn/hxmap/get_bank.jsp?jsonpcallback=callback&params.proNo=ANH&params.branchCode=340100&params.bankName=&params.bankType=0&page=2&params.status=1&_=1563286964843']

        
    return page_websites


# 获取一页的数据
def getPageData(url):
    print(url)
    global session
    res = session.get(url,headers=theHeaders);

    text = res.text;

    # 找出json字符串
    data = re.findall(r"[\s\S]*callback\(([\s\S]*)\)[\s\S]*", text)[0];
    # 删除无关文字
    data1 = re.sub(r'[\r\n\t\s    ]', '', data)
    # 替换不规则json,数组后面多了个逗号，会解析失败
    data2 = data1.replace(",]}", "]}")
    print(data2)
    # print(json.loads(re.sub(r'[\r\n\t\s    ]', '', data)))


    return json.loads(data2).get('list')




# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('hxb.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])

    for bank in bankData:

        writer.writerow([bank.get('bankName'), bank.get('address'), bank.get('bankTel'),bank.get('posYX').split(",")[0],bank.get('posYX').split(",")[1]])
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


