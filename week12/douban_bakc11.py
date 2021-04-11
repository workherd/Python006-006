# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from doubanmovie.items import DoubanmovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'  # 爬虫的名字
    allowed_domains = ['douban.com']  # 爬取的范围
    start_urls = ['http://douban.com/']  # 起始url

    # def parse(self, response):
    #     pass
    def start_requests(self):
        for i in range(1, 10):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  # 解析函数
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'hd'})
        for i in title_list:
            item = DoubanmovieItem()
            title = i.find('a').find('span').text
            link = i.find('a').get('href')
            item['title'] = title
            item['link'] = link
            # yield item

            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):  # 解析页面
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item
