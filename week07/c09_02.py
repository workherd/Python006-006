#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:20
# @Author     : john
# @File       : c09.py
# 不定长参数

def outer2(func):
    def inner(*args, **kwargs):
        print(args)
        print(type(args))
        print(type(kwargs))
        for i in args:
            print(i)
        func(*args, **kwargs)
    return inner


@outer2
def foo(a, b, c):
    print(a+b+c)


foo(1, 2, 4)
a = foo.__name__
print(a)