import requests


from pyquery import PyQuery as pq
import csv
import time
import random
import codecs


# 把所有链接生成出来
def get_page_urls():
    base_url = 'http://app.abchina.com/branch/common/BranchService.svc/Branch?p=340000&c=340100&b=-1&q=&t=1&z=0&i='


    page_websites = []
    page_count = 6
  
    for i in range(page_count):
    
        url = base_url+str(i)    
        page_websites.append(url)
        
    return page_websites


# 获取一页的数据
def getPageData(url):

    doc = requests.get(url).json()
    # print(doc.get('BranchSearchRests'))
    branchSearchRests = doc.get('BranchSearchRests');
    banks = []
   
    for branchSearchRest in branchSearchRests:
      
        bank = branchSearchRest.get('BranchBank')
       
        banks.append(bank)
  
    return banks

# 保存到csv文件。乱码处理
def toFile(bankData):
    # print(bankData)
    f = codecs.open('abchina.csv','w','utf_8_sig')
    writer = csv.writer(f)
    writer.writerow(['网点名称', '网点地址', '电话','Longitude','Latitude'])
    for bank in bankData:
        writer.writerow([bank['Name'], bank['Address'], bank['PhoneNumber'],bank['Longitude'],bank['Latitude']])
    f.close()
                  
    

def init():
    page_websites = get_page_urls();
    # print(page_websites);
   
    bankData = [];
    first = page_websites[0];
    for url in page_websites:
        pageData = getPageData(url)

        bankData += pageData
        time.sleep(1+random.randint(1,50)/100)
    toFile(bankData)
    
    # toFile(getPageData(first))

init()


