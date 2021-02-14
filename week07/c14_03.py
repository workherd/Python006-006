#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 15:31
# @Author     : john
# @File       : c14_03.py

alist = [1, 2, 3, 4, 5]

a = hasattr(alist, '__iter__')  # true
print(a)

a = hasattr(alist, '__next__')  # false
print(a)

# 结论： 列表是可迭对象，不是迭代器
# __iter__方法是iter（）函数对应的魔术方法
# __next__方法是next（）函数对应的魔术方法
#
for i in alist:
    print(i)

