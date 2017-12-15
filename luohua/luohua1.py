import requests
from lxml import html
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
def get_page_urls():
    base_url = 'http://www.luohua02.org/dm/'
    # base_url = 'http://www.runningls.com/demos'
    # /home/' + num
    response = requests.get(base_url,headers=headers).content

    soup = BeautifulSoup(response,'html.parser',from_encoding="gb18030")
    page = soup.find('div',class_='page')
    page_count = int(page.findAll('a')[-2].get_text()); 
    # print(a)



    # print(response)
    page_websites = []
    

    # page_count = page_count.split('/')[-1]
    #这里重复构造变量，主要是为了获取图片总数。更高级的方法是使用函数间的传值，但是我忘了怎么写了，所以用了个笨办法。欢迎大家修改
    #构建图片具体地址的容器
    # for i in range(int(page_count)):
    for i in range(page_count):
        if i == 0:
            url = base_url
        else:
            num = i+1
            url = base_url+'/index/'+str(num)+'.html'
        page_websites.append(url)

    return page_websites




def download_image(url,key):
    response = requests.get(url).content
    soup = BeautifulSoup(response,'html.parser',from_encoding="gb18030")
    
    tus= soup.findAll('div',class_='tu')

    for tu in tus:
        img = tu.find('img'); 
        print(img)
        title = './luohua_img/'+str(key+1)+img['alt']+'.jpg'
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
        with open(title, 'wb') as f:
            # # try:
            f.write(requests.get(src).content)
            # except IOError:
            #     print "Error: 没有找到文件或读取文件失败"
            # else:
            #     print "内容写入文件成功"
                
            



    #将图片保存到本地。传入的两个参数是图片的标题，和下载地址序列
    # num = 1
    # amount = len(image_detail_websites)
    # #获取图片总数
    # for i in image_detail_websites:
    #     filename = '%s%s.jpg' % (image_title, num)
    #     print('正在下载图片：%s第%s/%s张，' % (image_title, num, amount))
    #     headers = {'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
    #         'Accept-Encoding':'gzip, deflate',
    #         'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    #         'Cache-Control':'no-cache',
    #         'Host':'img.mmjpg.com',
    #         'Proxy-Connection':'keep-alive',
    #         'Referer':i,
    #         'Upgrade-Insecure-Requests':'1',
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
    #     with open(filename, 'wb') as f:
    #         f.write(requests.get(i, headers=headers).content)
    #     num += 1


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
