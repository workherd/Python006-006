#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:35
# @Author     : john
# @File       : c09_03.py

# 被iushi函数带返回值

def outer3(func):  # 装饰器的框架
    def inner3(*args, **kwargs):
        print(type(args))
        print('before')
        ret = func(*args, **kwargs)
        print('after')
        return ret
    return inner3


@outer3
def foo3(a, b, c):

    return (a+b+c)

print(foo3(1, 3, 5))

