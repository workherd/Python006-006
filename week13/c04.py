#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 14:04
# @Author     : john
# @File       : c04.py
# http协议的GET方法
import requests
r = requests.get('https://github.com')
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
# print(r.json())

# http协议的POST方法
import requests
r =  requests.post('http://httpbin.org/post', data= {'key':'value'})
print(r.json())