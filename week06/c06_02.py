#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 19:01
# @Author     : john
# @File       : c.py
class Human2(object):
    """ 同时存在的调用顺序"""

    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        print('Human2:__getattr__')
        return 'Err 404, 你请求的参数不存在'

    def __getattribute__(self, item):
        print('Human2:__getattribute__')
        return super().__getattribute__(item)


h1 = Human2()
# 若同事存在 __getattribute__》__getattr__》__dict__
print(h1.age)
print(h1.noattr)  # 注意调用顺序