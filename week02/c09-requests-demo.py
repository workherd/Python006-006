#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import requests
from fake_useragent import UserAgent

"""
模拟登陆
需要关注的东西
step1：
Request URL: https://accounts.douban.com/j/mobile/login/basic
Request Method: POST
step2:
Host: accounts.douban.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Referer: https://accounts.douban.com/passport/login?source=movie

"""

ua = UserAgent(verify_ssl=False)
headers = {
    'User-Agent': ua.random,
    'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象：在同一个Session 实例发出的所有请求之间保持cookie
# 期间使用urllib3 的 connection pooling 功能
# 向同一主机发送多个请求，底层的 TCP 连接将被重用 从而带来显著的性能提升

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck':'',
    'remember':'true',
    'name':'1330430077@qq.com',
    'password':'douban#1234'
}

response = s.post(login_url,data=form_data,headers=headers)
print(response.text)
# 登录后可以进行后续的请求
# url2 = https://accounts.douban.com/passport/setting

# response2 = s.get(url2,headers = headers)
# response3 = newsession.get(url3,headers = headers, cookies = s.cookies)
#
# with open('profile.html','w+') as f:
#     f.write(response2.text)
with open('douban_login.html','w+') as f:
    f.write(response.text)