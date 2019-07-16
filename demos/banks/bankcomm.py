import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs

from urllib import parse


# 交通银行
session = requests.Session()
theHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'www.bankcomm.com',

}



# 获取一页的数据
def getPageData(url):
    print(url)
    global session
    res = session.get(url,headers=theHeaders);
    
    doc = res.json()
  

    data = doc.get('data')



   
    return data

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('bankcomm.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])
   
    # 遍历字典
    for key in bankData:
        writer.writerow([bankData[key].get('n'), parse.unquote(bankData[key].get('a')), bankData[key].get('o'),bankData[key].get('x'),bankData[key].get('y')])
    f.close()
                  
    

def init():
    url = 'http://www.bankcomm.com/BankCommSite/zonghang/cn/node/queryBranchResult.do'
    pageData = getPageData(url)
    toFile(pageData)

init()


