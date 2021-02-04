#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 19:56
# @Author     : john
# @File       : c09_01_single.py
# 装饰器实现单实例模式
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class MyClass:
    pass


m1 = MyClass()
m2 = MyClass()
print(id(m1))
print(id(m2))