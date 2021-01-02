#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pathlib import *
import sys
import time
from selenium import webdriver


"""

https://www.zhihu.com/api/v4/questions/26551475/root_comments?limit=10&offset=30&order=normal&status=open

使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件。
https://www.zhihu.com/question/421150601

referer: https://www.zhihu.com/question/421150601
method:post

用户：//div[@class="List-item"]//a[@class="UserLink-link"]/text()
答案://div[@class="List-item"]//div[@class="RichContent-inner"]/span[1]/p/text()
答案的规则： span 标签  类class  =  "RichText ztext CopyrightRichText-richText"
"""
#
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
#              '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
#
# header = {'user-agent':user_agent}
#
# my_url = 'https://www.zhihu.com/question/421150601'
#
# try:
#     response = requests.get(my_url,headers=header,timeout=20.001)
# except requests.exceptions.ConnectTimeout as e:
#     print(f'requests 库超时.\n{e}')
#     sys.exit(1)
#
# # 将获取的网页打印出来
# try:
#     with open('zhihu_qa.html','w',encoding='utf-8') as f:
#         f.write(response.text)
# except Exception as e:
#     print('e')
#
#
# headers_2 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
#              '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
#
#
# }
#
# headers_3 = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
#              '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
#     'Referer': 'https://www.zhihu.com/question/421150601',
#     'x-za-clientid': '9698a2b3-cdd8-433e-9f44-2c2eace1b8bd'
#
# }
#
# my_url_sep1 = 'https://zhihu-web-analytics.zhihu.com/api/v2/za/logs/batch'
# my_url_sep2 = 'https://zhihu-web-analytics.zhihu.com/api/v2/za/logs/batch'


# 会话对象：在同一个Session 实例发出的所有请求之间保持cookie
# 期间使用urllib3 的 connection pooling 功能
# 向同一主机发送多个请求，底层的 TCP 连接将被重用 从而带来显著的性能提升
#
# login_url = 'https://accounts.douban.com/j/mobile/login/basic'
#
#
# for i in range(5):
#     s = requests.Session()
#     time.sleep(1)
#     print(f'第{i}次获取答案')
#     ret = s.options(my_url_sep1,headers=headers_2)
#     print(ret.status_code)
#     s = requests.Session()
#     ret = s.post(my_url_sep1,headers=headers_3)
#     print(ret.status_code)
#     with open('zhihu_qa.html','a',encoding='utf-8') as f:
#         print(ret.text)
#         f.write(ret.text)
#
# print('end')


# # 获取pythoe脚本的绝对路径
# p = Path(__file__)
# print('路径为',p)
#
# pyfile_path = p.resolve().parent
# print(pyfile_path)
#
# # 建立新的目录html
# html_path = pyfile_path.joinpath('html')
# if not html_path.is_dir():
#     Path.mkdir(html_path)
# page = html_path.joinpath('douban.html')
#
# # 上下文管理器
# try:
#     with open(page,'w',encoding='utf-8') as f:
#         f.write(response.text)
# except FileNotFoundError as e:
#     print(f'文件无法打开{e}')
# except IOError as e:
#     print(f'读写文件出错{e}')
# except Exception as e:
#     print(e)
#
# print(f'返回码是：{response.status_code}')
# print(f'返回码是：{ret.status_code}')


# starter


if __name__ == '__main__':
    drive = webdriver.Chrome()  # 打开浏览器
    drive.get("https://www.zhihu.com/question/421150601")

    #