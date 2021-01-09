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
    # content = selector.xpath('//div[@class="p_mainnew"]/text()[last()]')
    # content = selector.xpath('//div[@class="p_mainnew"]/text()[last()]')
    # content = selector.xpath('//div[@class="p_content"][1]').xpath('string(.)').extract()[0]
    # content = selector.xpath('//div[@class="p_mainnew"]/text()').xpath('string(.)').extract()[0]
    # content = selector.xpath('//div[@class="p_mainnew"]/text()[last()]')

    # content = content1[0].xpath('string(.)').strip()

    content1 = selector.xpath('//div[@class="p_mainnew"]')
    content = content1[1].xpath('string(.)').strip()

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
# import re
#
# str1 = ' </a> 华为在 1 月 1 日凌晨发布公告宣布下架腾讯手游。腾讯按市值是世界最大的游戏公司。华为给出的理由是“腾讯游戏于 2020 年 12 月 31 日 17 点 57 分单方面就双方合作做出重大变更，导致双方的继续合作产生重大障碍。经过我司法务的谨慎评估，我们不得不依照腾讯单方面要求暂停相关合作，将腾讯游戏从华为平台下架。对此我们深表遗憾。”业内人士称<a href="https://news.stcn.com/sd/202101/t20210101_2693963.html">腾讯与华为之间的分歧是平台抽成比例</a>。苹果和 Google 应用商店的抽成比例是 30%，这一比例被认为过高而引发了很多争议，Epic Games 为此与苹果在打官司。但与中国的平台相比，30% 已经是很低了。国产 Android 机官方应用商店一直跟游戏厂商 5:5 分成，这还是在扣除支付通道费之后算的，所以游戏厂商实际只能拿到不足 50% 的分成。也就是说，开发商辛辛苦苦做一个游戏，大部分的收入都会被渠道赚走。   '
# print(f'str1:{str1}')
# str2 = re.sub("<a href=.*\">", '', str1)
# str3 = re.sub("\S</a>", '', str2)
# print(f'str3:{str3}')
# str3 = ""
# for i in t:
#     str3 += i
#
# print(f'str1:{str3}')


if __name__ == '__main__':
    url = 'https://www.solidot.org/'
    get_info(url)
