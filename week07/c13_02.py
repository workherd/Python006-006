#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 14:28
# @Author     : john
# @File       : c13_02.py

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):  # 人为看的形式
        return f'hello, {self.first_name} {self.last_name} __str'

    def __repr__(self): # 遵循原有内容输出,对象调用的时候调用
        return f'hello, {self.first_name} {self.last_name} __repr'


me = Person('li', 'john')
print(f'{me}')