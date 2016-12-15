import scrapy


class aSpider(scrapy.Spider):
    name = "a"
    def start_requests(self):
        urls = [
            'http://baike.baidu.com/view/1406677.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield scrapy.Request(url='http://baike.baidu.com/view/706340.htm', callback=self.end)

    def end(self,response):
        pass
