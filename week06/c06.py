#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 19:01
# @Author     : john
# @File       : c.py
class Human2(object):
    """ getattribute对任意属性进行截获"""

    def __init__(self):
        self.age = 18

    def __getattr__(self, item):
        # 对指定属性做处理, fly 属性返回‘superman’，其他属性返回none
        self.item = item
        if self.item == 'fly':
            return 'superman'


h1 = Human2()
print(h1.age)
print(h1.fly)
print(h1.noattr)
print(h1.__dict__)