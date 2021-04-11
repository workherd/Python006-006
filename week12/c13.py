#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/20 20:22
# @Author     : john
# @File       : c13.py

def chain(num):
    for it in range(num):
        yield it


num = 5
y = chain(num)
print(y)
print(type(y))

print(next(y))
print(next(y))
print(next(y))
print(list(y))
next(y)
print(next(y))

