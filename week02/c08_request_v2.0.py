#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pathlib import *
import sys

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
header = {'user-agent':user_agent}

my_url = 'https://movie.douban.com/top250'

try:
    response = requests.get(my_url,headers=header)
except response.exceptions.ConnectTimeout as e:
    print('requests 库超时')
    sys.exit(1)

# 将网页存入文件
# print(response.text)

# 获取

print(f'返回码是：{response.status_code}')
