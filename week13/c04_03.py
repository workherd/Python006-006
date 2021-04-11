#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 15:35
# @Author     : john
# @File       : c04_03.py
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers ={
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}
s = requests.Session()
# 回话对象，session实例，保持cookie，期间使用urllib3的connection pooling功能
# 向统一注意发送多个请求，底层的tcp连接将被重用，从而带来显著的性能提升

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '1330430077@qq.com',
    'password': 'test123123',
    'remember': 'false',
    'ticket': ''
}

response = s.post(login_url, data= form_data, headers=headers)

print(response.text)

# 登录后可以进行后续的请求

url2 = 'https:///accounts.douban.com/passport/setting'
response2 = s.get(url2, headers=headers)
# response3 = newsession.get(url3, headers=headers, cookies=s.cookies)
with open('profile.html', 'w+') as f:
    f.write(response2.text)