#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:10
# @Author     : john
# @File       : c01.py


gennumber = (i for i in range(0,2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))
except StopIteration:
    print('最后一个元素')