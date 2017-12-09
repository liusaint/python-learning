import scrapy


class QuotesSpider(scrapy.Spider):
    name = "blog"

    def start_requests(self):
        urls = [
            'http://blog.csdn.net/liusaint1992',            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        articles = response.css("div.article_item")
        articleList = []
        for article in articles:
            title = article.css(".link_title a::text").extract_first().strip()
            content = article.css(".article_description::text").extract_first().strip()
            articleD = {"title":title,"content":content}
            print(articleD)
            yield articleD
            # articleList.append(articleD)
         
        next_page = response.css("#papelist strong+a::attr(href)");
        if next_page is not None:
          yield response.follow(next_page[0],self.parse)    
          # return articleList
