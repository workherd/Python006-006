import scrapy


class MovicesSpider(scrapy.Spider):
    name = 'movices'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
