#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 14:09
# @Author     : john
# @File       : c04_02.py
import requests
# 在一个session实例发出的所有请求之间保持cookie
s=requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456790')
r=s.get('http://httpbin.org/cookies')

print(r.text)

# 回话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cokies/set/sessioncookie/123456789')


