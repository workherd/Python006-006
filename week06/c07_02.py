#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/28 18:24
# @Author     : john
# @File       : c07_02.py

class Human(object):
    def __init__(self, name):
        self.name = name

    # 将方法封装成属性 # 方法调用 #
    @property
    def gender(self):
        return 'M'


h1 = Human('Adam')
h2 = Human('Eva')
print(h1.gender)

h2.gender = 'F'  # 只有只读的功能，此处赋值会报错
