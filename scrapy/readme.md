* 新建项目：scrapy startproject project_name
* spider下创建文件。
* class QuotesSpider(scrapy.Spider):
* 到项目顶层去运行　scrapy crawl quotes
* response.css('title::text').extract()
* response.css('title::text').extract_first() 提取文本内容。
* response.css('li.next a::attr(href)').extract_first()。获取属性。
* 层级搜索　quote = response.css("div.quote")[0]　　title = quote.css("span.text::text").extract_first()
* scrapy crawl quotes -o quotes.json  导出到文件。运行两次会append到后面。
*         next_page = response.urljoin(next_page) yield scrapy.Request(next_page, callback=self.parse) 
* response.follow可以传入相对链接也可以传入a标签。response.follow(response.css('li.next a')[0])
* 默认会过滤重复url