#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/28 19:42
# @Author     : john
# @File       : c08.py
class People(object):
    def __init__(self):
        self.gene = 'XY'

    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self, name):
        self.name = name

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self, name):
        self.name = name

    def shopping(self):
        print('buy buy buy')


p1 = Man('Adam')
p2 = Woman('Eve')

# gene 是否有继承 # 没有继承 初始化函数覆盖了
print(p1.gene)
