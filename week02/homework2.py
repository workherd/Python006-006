#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from pathlib import *
import sys
import time
from fake_useragent import UserAgent
from lxml import etree
import re
"""
https://www.solidot.org/
"""


def get_info(url):
    ua = UserAgent(verify_ssl=False)
    headers = {
        'User-Agent': ua.random,
    }
    # s = requests.Session()
    # # 会话对象：在同一个Session 实例发出的所有请求之间保持cookie
    # # 期间使用urllib3 的 connection pooling 功能
    # # 向同一主机发送多个请求，底层的 TCP 连接将被重用 从而带来显著的性能提升

    response = requests.get(url, headers=headers)
    # print(reponse.text)
    with open('homework2_tmp.txt','w',encoding='utf-8') as f:
        f.write(response.text)

    # str1 = response.text
    # str2 = re.sub("<a href=.*\">", '', str1)
    # str3 = re.sub("\S</a>", '', str2)
    # selector = etree.HTML(str3)
    selector = etree.HTML(response.text)

    title = selector.xpath('//div[@class="bg_htit"]/h2/a/text()')
    content = selector.xpath('//div[@class="p_mainnew"]/text()[last()]')
    # content1 = selector.xpath('//div[@class="p_content"]/div[1]')
    # content = content1.xpath('string(.)').extract()[0]

    solidot_info = dict(zip(title,content))
    # print(type(solidot_info))
    print(solidot_info)

    for i in solidot_info:
        with open('homework2_result.txt', 'a',encoding='utf-8') as f:
            s = str(i) + "\n" + str(solidot_info[i]) + "\n"
            f.write(s)

#
# lis=ul.xpath('./li[@data-title]')
# movies=[]
# for li in lis:
#     title=li.xpath('@data-title')[0]
#     score=li.xpath('@data-rate')[0]
#     duration=li.xpath('@data-duration')[0]
#     region=li.xpath('@data-region')[0]
#     director=li.xpath('@data-director')[0]
#     actors=li.xpath('@data-actors')[0]
#     thumbnail=li.xpath('.//img/@src')[0]
#     movie={
#         'title':title,
#         'score':score,
#         'duration':duration,
#         'region':region,
#         'director':director,
#         'actors':actors,
#         'thumbnail':thumbnail
#     }
#     movies.append(movie)
#


if __name__ == '__main__':
    url = 'https://www.solidot.org/'
    get_info(url)
