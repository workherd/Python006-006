#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests

# http协议的GET方法
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']
# r.text
r.encoding
# r.json()

# http 协议的 POST 方法
r = requests.post('http://httpbin.org/post',data = {'key':'value'})
a = r.json()
print(a)

print('*'*88)
print('use session')
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/12345678')
r = s.get('http://httpbin.org/cookies')
print(r.text)

print('*'*88)
print('with open')
# 可以使用会话上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/12345678')