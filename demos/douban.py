
import requests
from lxml import html


# https://book.douban.com/subject_search?search_text=python&cat=1001&start=0
# 下载豆瓣查询python。

base_url = 'https://book.douban.com/subject_search?search_text=python&cat=1001&start=';
page_size = 15
def down_page(num):
	url = base_url + str((num-1)*10)
	response = requests.get(url).content
	selector = html.fromstring(response) 
	div = selector.xpath("//div[@class='item-root']")
	# 找不到，动态渲染

	print(div)


down_page(1)
