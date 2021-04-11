#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 13:47
# @Author     : john
# @File       : c03.py

from fake_useragent import  UserAgent

ua = UserAgent(verify_ssl=False)

#模拟不同的浏览器
print(f'Chrome 浏览器：{ua.chrome}')
print(f'safari 浏览器: {ua.safari}')
print(f'ie 浏览器: {ua.ie}')

# 随机值
print(f'随机浏览器：{ua.random}')