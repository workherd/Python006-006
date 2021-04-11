#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/20 7:57
# @Author     : john
# @File       : c04_pagedown.py
import time
import requests
from bs4 import BeautifulSoup as bs


def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

    header = {'user-agent':user_agent}
    response = requests.get(myurl, headers=header)
    # bs_info = bs(response.text, 'html.parse', from_encoding='utf-8')
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
        for atag in tags.find_all('a', ):
            print(atag.get('href'))
            print(atag.find('span', ).text)


urls = tuple(f'https://movie.douban.com/top250?start={page*25 }&filter=' for page in range(10))
print(urls)

time.sleep(3)

for page in urls:
    get_url_name(page)
    time.sleep(5)

