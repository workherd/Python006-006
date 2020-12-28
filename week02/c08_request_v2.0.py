#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pathlib import *
import sys


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
header = {'user-agent':user_agent}

my_url = 'https://movie.douban.com/top250'

try:
    response = requests.get(my_url,headers=header,timeout=1.001)
except requests.exceptions.ConnectTimeout as e:
    print(f'requests 库超时.\n{e}')
    sys.exit(1)

# 将网页存入文件
# print(response.text)

# 获取pythoe脚本的绝对路径
p = Path(__file__)
print(p)

pyfile_path = p.resolve().parent
print(pyfile_path)

# 建立新的目录html
html_path = pyfile_path.joinpath('html')
if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

# 上下文管理器
try:
    with open(page,'w',encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f'文件无法打开{e}')
except IOError as e:
    print(f'读写文件出错{e}')
except Exception as e:
    print(e)

print(f'返回码是：{response.status_code}')
