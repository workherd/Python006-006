# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
from doubanmovie.items import DoubanmovieItem
from scrapy.selector import Selector


class DoubanSpider(scrapy.Spider):
    name = 'douban'  # 爬虫的名字
    allowed_domains = ['douban.com']  # 爬取的范围
    start_urls = ['http://douban.com/']  # 起始url

    # def parse(self, response):
    #     pass
    def start_requests(self):
        for i in range(0, 10):
            # i = 0
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)  # false 表示去重    设置成重 True，将不会去重，直接发送请求

    def parse(self, response):  # 解析函数
        print('>>>>>>>>>>>>>>>>>>>>>>>>', response.url)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movices = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movices:
            item = DoubanmovieItem()
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')
            # print('-'*88)
            # print(title)
            # print(link)  # 带格式的
            # print('-'*88)
            # print(title.extract())
            # print(link.extract())
            # print('-'*88)
            # print(title.extract_first())
            # print(link.extract_first())
            item['title'] = title.extract_first().strip()
            item['link'] = link.extract_first().strip()
            print('-'*88)
            print(title.extract_first().strip())
            print(link.extract_first().strip())
            yield item