#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 18:58
# @Author     : john
# @File       : c05.py


class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):  # 接受参数
        # 普通字段
        self.name = name  # self 表示示例化本身， 可以改成任意字符，但建议保持
        # print("object init", self.name)

h1 = Human('Adam')
h2 = Human('Eve')


print(h1.name)
del h1.name

print(h1.name)