#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/15 1:43
# @Author     : john
# @File       : c02_bs4.py
# 使用beautifulSoup解析网页

import time
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

bs_info = bs(response.text, 'html.parser')  # 默认的解析方式，但效率不高

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        print(atag.find('span',).text)
