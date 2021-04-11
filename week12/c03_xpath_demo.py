#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/15 2:16
# @Author     : john
# @File       : c03_xpath_demo.py

import requests
import pandas as pd
import lxml.etree

url = 'https://movie.douban.com/subject/1292052/'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'


header = {}

header['user-agent'] = user_agent
reponse = requests.get(url, headers=header)

selector = lxml.etree.HTML(reponse.text)

film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')

print(f'电影名称为：{film_name}')

plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映时间： {plan_date}')

rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分: {rating}')

mylist = [film_name, plan_date, rating]

movie1 = pd.DataFrame(data=mylist)
movie1.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)
