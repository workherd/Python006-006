#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
r = requests.get('http://www.httpbin.org/')
print(r)

# 传递get参数
payload = {'key1':'value1','key2':'value2','key3':'value3'}
r1 = requests.get('http://www.httpbin.org/',params=payload)
print(r1.url)


