#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 12:52
# @Author     : john
# @File       : c06_03.py
# map 用前面的值依次处理
def square(x):
    return x**2


m = map(square, range(10))
print(m)
a = next(m)  # 取下一个值
print(a)
print(next(m))
a = list(m)  # 取所有的值
print(a)

a = [square(x) for x in range(10)]
print(a)
a = dir(m)
print(a)


from functools import reduce  # 函数作用，将右侧参数按照左边函数 两两操作


def add(x, y):
    return x + y


a= reduce(add, [1, 3, 5, 7, 9])
print( reduce(add, [1, 3, 5, 7, 9]) )
print(a)


# filter
def is_odd(n):
    return n % 2 == 1

a = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(a)


# 偏函数, 要产生一个函数的新名字
def add(x, y):
    return x + y

import functools
add_1 = functools.partial(add, 1)
a = add_1(10)
print(a)

import itertools
g = itertools.count()
a = next(g)
print(a)

a = next(g)
print(a)

auto_add_1 = functools.partial(next, g)
a = auto_add_1()
print(a)
a = auto_add_1()
print(a)
"""
itertools: https://docs.python.org/3/library/itertools.html
functools: https://docs.python.org/3/library/functools.html
operator: https://docs.python.org/3/library/operator.html
"""