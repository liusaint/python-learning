import requests
from bs4 import BeautifulSoup




# 豆瓣250

base_url = 'https://movie.douban.com/top250?start=';
page_size = 25
data = []
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'ll="108296"; bid=kqT2X3wQIDc; gr_user_id=fa3226c6-88ad-42e7-911a-1ac4935f82b5; _vwo_uuid_v2=69404A212D416F300358474A0DAD66FA|7aa169afb4c5a42655646c3648bdc1bb; __utma=30149280.608752988.1502192089.1513493026.1513497201.7; __utmc=30149280; __utmz=30149280.1513319293.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; as="https://sec.douban.com/b?r=https%3A%2F%2Fmovie.douban.com%2Ftop250%3Fstart%3D0"; ps=y',
'Host':'sec.douban.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
def down_page(num):
	url = base_url + str((num-1)*page_size)
	response = requests.get(url,headers=headers).content
	print(url)
	soup = BeautifulSoup(response,'html.parser',from_encoding="utf-8") 

	ol = soup.find('ol',class_="grid_view")
	lis = ol.findAll('li');

	
	for li in lis:
		li_data = {}
		li_data['id'] = li.find('em').get_text()
		li_data['img']= li.find('img')['src']
		li_data['title'] = li.select('div.hd .title')[0].get_text()
		li_data['star'] = li.select('.rating_num')[0].get_text()
		li_data['short'] = li.select('.inq')[0].get_text().encode('utf-8', 'ignore').decode('utf-8','ignore');
		data.append(li_data)
	# print(data,num)
	

# down_page(1)

def get_urls():
	url = base_url + '0'
	response = requests.get(url,headers=headers).content

	soup = BeautifulSoup(response,'html.parser',from_encoding="utf-8") 

	page_count = soup.select(".paginator a")[-2].get_text()

	for i in range(int(page_count)):
		down_page(i+1)

	# print(data)
	html = "<html>"
	html += "<body>"
	html += "<table>"
	html = html + "<tr><th>序号</th><th>标题</th><th>评分</th><th>摘要</th></tr>"
	for val in data:
		
		# 不能写成val.id!!!
		html = html + "<tr><td>"+val['id']+"</td><td>"+val['title']+"</td><td>"+val['star']+"</td><td>"+val['short']+"</td></tr>"
	html+= "</table>"
	html +="</body>"
	html +="</html>"

	try:
		with open('output.html', 'wb') as f:
			try:
				f.write(html)
			except:
				print ("Error: 没有找到文件或读取文件失败")
	except:
		print('error')


	


get_urls()
