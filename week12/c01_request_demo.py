#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/15 1:14
# @Author     : john
# @File       : c01_request_demo.py
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
             ' (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)
print(response.text)
print(f'返回码{response.status_code}')