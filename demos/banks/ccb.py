import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs


session = requests.Session()
theHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Host': 'www.ccb.com',

}

# 把所有链接生成出来
def get_page_urls():

    res1 = session.get('http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=100119',headers=theHeaders)
 


    base_url = 'http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=NZX010&ADiv_Cd=340100&Kywd_List_Cntnt=&Enqr_MtdCd=4&PAGE='


    page_websites = []
    page_count = 52
  
    for i in range(page_count):
    
        url = base_url+str(i+1)    
        page_websites.append(url)
        
    return page_websites


# 获取一页的数据
def getPageData(url):
    print(url)
    global session
    res = session.get(url,headers=theHeaders);
    if res.status_code == 200:
        doc = res.json()
    else:
        session = requests.Session()
        print(res.status_code)
        print(res.content)
        return getPageData(url)
    # print(doc.get('BranchSearchRests'))

    branchSearchRests1 = doc.get('OUTLET_DTL_LIST')
    branchSearchRests1.pop()
    branchSearchRests2 = doc.get('SLFBANK_DTL_LIST')
    branchSearchRests2.pop()
    branchSearchRests3 = doc.get('SLFEQMT_DTL_LIST')
    branchSearchRests3.pop()
    banks = branchSearchRests1 + branchSearchRests2 +branchSearchRests3


   
    return banks

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('ccb.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])
    # 使用.get避免读取不存在的属性时报错https://www.polarxiong.com/archives/Python-%E6%93%8D%E4%BD%9Cdict%E6%97%B6%E9%81%BF%E5%85%8D%E5%87%BA%E7%8E%B0KeyError%E7%9A%84%E5%87%A0%E7%A7%8D%E6%96%B9%E6%B3%95.html
    for bank in bankData:
        writer.writerow([bank.get('CCBIns_Nm') or bank.get('MtIt_Nm') or bank.get('MtIt_Nm'), bank.get('Dtl_Adr'), bank.get('Fix_TelNo'),bank.get('Lgt'),bank.get('Ltt')])
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


