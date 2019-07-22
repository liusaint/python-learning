import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs
import urllib3
urllib3.disable_warnings()


session = requests.Session()
session.cert = './a.cert'
theHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'www.spdb.com.cn',
    'Origin': 'https://www.spdb.com.cn',
   
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cookie': 'firstLoad=no; TSPD_101=08e305e14cab280025e77935cca493f31f5504405376d31e9be6176f88a62103c9f80f314d56084ab4fcebb020bac8ad085bd009b00510003c8f0315a891e12d32604c0555697ae8; WASSESSION=KYHru-78sq5nwIz6bcfp__DIuTqWlLAKmmoGU-L5r86Q6kcthMnO!1727271355; TS01d02f4c=01ea722d2afbaf5bbd7083e60b4925ba093ba6492175da0d30e05085f53ee680bb236e595896ec16307957702a6bdd2265421099f23fc0c1e1045cb76c9b01a480ef07245e',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

# 把所有链接生成出来
def get_post_data():

 


    base_url = 'https://www.spdb.com.cn/was5/web/search'

    postData = [{
        'metadata': 'deptinfo_orgid|deptinfo_name|deptinfo_address|deptinfo_postcode|deptinfo_telno|deptinfo_longitude|deptinfo_dimensions',
        'channelid': 243263,
        'page': 1,
        'searchword': '((deptinfo_address,deptinfo_name)+=%)*(deptinfo_province=%安徽省%)*(deptinfo_city=%合肥市%)'
    }]
    
    page_count = 17
  
    for i in range(page_count):
    
        item = {
            'metadata': 'atminfo_branchname|atminfo_adress|atminfo_orgid|atminfo_termtype|atminfo_longitude|atminfo_dimensions|atminfo_telno|atminfo_atmno',
            'channelid': 284746,
            'page': i+1,
            'searchword': '(atminfo_branchname=%)*(atminfo_province=%安徽省%)*(atminfo_city=%合肥市%)'
        }    
        postData.append(item)
        
    return postData


# 获取一页的数据
def getPageData(postData):
    url = 'https://www.spdb.com.cn/was5/web/search'
    global session
    print(postData)
    print(theHeaders)
    res = session.post(url,data=postData,headers=theHeaders)
    print(res.content)
    return res.json().get('rows')

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('sqdb.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])

    for bank in bankData:
        writer.writerow([bank.get('atminfo_branchname') or bank.get('deptinfo_name') , bank.get('atminfo_adress') or bank.get('deptinfo_address'), bank.get('atminfo_telno') or bank.get('deptinfo_telno'),bank.get('atminfo_longitude') or bank.get('deptinfo_longitude'),bank.get('atminfo_dimensions') or bank.get('deptinfo_dimensions')])
    f.close()
                  
    

def init():
    postDatas = get_post_data();

   
    bankData = [];
    
    for data in postDatas:
        pageData = getPageData(data)
        
        bankData += pageData
        time.sleep(1+random.randint(1,50)/100)

    toFile(bankData)
    
    # toFile(getPageData(first))

init()


