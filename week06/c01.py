#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 14:47
# @Author     : john
# @File       : c01.py


class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):  # 接受参数
        # 普通字段
        self.name = name  # self 表示示例化本身， 可以改成任意字符，但建议保持
        print("object init", self.name)


man = Human('Adam')
woman = Human('Eve')

# 查看类属性
a = Human.__dict__
print(a)
print(man.name)
man.live = False
a = man.__dict__
print('man dict',a)
print('woman dict', woman.__dict__ )