#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from lxml import etree
from time import sleep

# 定义函数
def get_url_name(myurl):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent': ua}
    reponse = requests.get(myurl, headers=header)
    print(reponse.text)
    selector = etree.HTML(reponse.text)
    # 电影名称列表
    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')

    # 电影的链接地址
    film_link = selector.xpath('//div[@class="hd"]/a/@href')

    # 遍历对应关系字典
    film_info = dict(zip(film_name, film_link))
    print(film_info)
    for i in film_info:
        print(f'电影名称：{i} \t \t 电影链接：{film_info[i]}')


if __name__ == '__main__':
    # 生成包含所有页面的元组
    urls = 'https://movie.douban.com/top250'
    print(urls)
    get_url_name(urls)
