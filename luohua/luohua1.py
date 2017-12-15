import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
def get_page_urls():
    # 动漫
    base_url = 'http://www.luohua02.org/dm/'

    response = requests.get(base_url,headers=headers).content

    soup = BeautifulSoup(response,'html.parser',from_encoding="gb18030")
    page = soup.find('div',class_='page')
    page_count = int(page.findAll('a')[-2].get_text()); 


    page_websites = []
    
    for i in range(page_count):
        if i == 0:
            url = base_url
        else:
            num = i+1
            url = base_url+'index'+str(num)+'.html'
        page_websites.append(url)

    return page_websites




def download_image(url,key):
    print(url)
    response = requests.get(url).content
    soup = BeautifulSoup(response,'html.parser',from_encoding="gb18030")
    
    tus= soup.findAll('div',class_='tu')

    for tu in tus:
        img = tu.find('img'); 
        print(img)
        title = './luohua_img/'+str(key)+img['alt']+'.jpg'
        src = 'http://www.luohua02.org'+img['src'];

        print('正在下载图片：%s，' % (title))
        print(src)
        # headers = {
        #     'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        #     'Accept-Encoding':'gzip, deflate',
        #     'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
        #     'Cache-Control':'no-cache',
        #     'Host':'img.mmjpg.com',
        #     'Proxy-Connection':'keep-alive',
        #     # 'Referer':src,
        #     'Upgrade-Insecure-Requests':'1',
        #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
        try:
            with open(title, 'wb') as f:
                try:
                    f.write(requests.get(src).content)
                except:
                    print ("Error: 没有找到文件或读取文件失败")
        except:
            print('error')
            # else:
            #     print "内容写入文件成功"
                           





if __name__ == '__main__':
    # page_number = input('请输入需要爬取的页码：')
    urls = get_page_urls()
    
    # link = get_page_number(page_number)[0]
    key = 1
    for url in urls:
        # for link in get_page_number(url):
    # for link in get_page_number(page_number):
    	
        download_image(url,key)
        key = key + 1
