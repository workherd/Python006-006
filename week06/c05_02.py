#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 19:01
# @Author     : john
# @File       : c.py
class Human2(object):
    """ getattribute对任意属性进行截获"""

    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print(f'__getattribute___ call item:{item}')


h1 = Human2()

print(h1.age)
print(h1.noattr)