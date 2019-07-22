import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs

from urllib import parse


# 平安银行  jsonp的解析 
session = requests.Session()
theHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'map.cmbchina.com',

}



# 获取一页的数据
def getPageData(url):
    print(url)
    global session
    res = session.get(url,headers=theHeaders);
    
    doc = res.json()
  

    data = doc.get('branches')



   
    return data

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('cmbchina.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])
   
    # 遍历字典
    for bank in bankData:
        writer.writerow([bank.get('name'), bank.get('address'), bank.get('tel'),bank.get('lng'),bank.get('lat')])
    f.close()
                  
    

def init():
    url = 'http://map.cmbchina.com/Service/branch.aspx?city=%u5408%u80A5&type=B&_=1563014307254&{}'
    pageData = getPageData(url)
    toFile(pageData)

init()


