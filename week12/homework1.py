#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/23 20:52
# @Author     : john
# @File       : homework1.py
"""
爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式
"""
import requests
from bs4 import BeautifulSoup as bs

myurl = 'https://maoyan.com/films?showType=3'
# myurl = 'http://192.168.56.11/maoyan/maoyang.html'
detail = 'https://maoyan.com/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
header = {'user-agent': user_agent,
          # 'cookie': '__mta=252449334.1616504042235.1616668345506.1616672161464.9; uuid_n_v=v1; uuid=D6BC50E08BD611EBA750FFCAF29D9B86D50EB2F1577B4FCCB6844236E68B8AAC; _csrf=885fc58e89b37cb9e85bfffbed4d0dd91887aba9ce7bdd53eab2b535bb1c9130; _lxsdk_cuid=1785f2632d9c8-0cf5773676abc5-3f604900-140000-1785f2632d9c8; _lxsdk=D6BC50E08BD611EBA750FFCAF29D9B86D50EB2F1577B4FCCB6844236E68B8AAC; __mta=252449334.1616504042235.1616668345506.1616671492220.9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1616623909,1616668343,1616671482,1616672161; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1616672161; _lxsdk_s=17869211fb6-24b-8db-2b2%7C%7C7',
}
response = requests.get(myurl, headers=header)
# print(response.text)
bs_info = bs(response.text, 'html.parser')

# for tags in bs_info.find_all('dd'):
#     for atag in tags.find_all('div', attrs={'class': 'movie-item-hover'}):
#         for a1 in atag.find_all('a'):
#             print('https://maoyan.com'+a1.get('href'))
#         for a2 in atag.find_all('div', attrs={'class'})

# for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
#     for tag in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
#         print(tag.find('span', ).text)

# for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
#     for tag in tags.find_all('span', attrs={'class': 'name'}):
#         print(tag.text)
#

# for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
#     for tag in tags.find_all('span', attrs={'class': 'name'}):
#         print(tag.text)

for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    for tag in tags.find_all('div'):
        print(tag.find('span',).text)
        print(tag.contents[0])


# for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
#     for tag11 in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
#         print(tag11.find('span',).text)
#         # print(tag11.)
