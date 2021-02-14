#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/14 11:34
# @Author     : john
# @File       : homework02.py

"""
自定义一个 python 函数，实现 map() 函数的功能。
"""


def my_map(func, args):
    t = []
    for i in args:
        # print(i)
        ret = func(i)
        # print(ret)
        t.append(ret)
    return t


def func1(a):
    str1 = str(a)
    return "func1+" + str1


if __name__ == '__main__':
    a = ['adb','ddd', 'cccc']
    ret2 = my_map(func1, a)
    print(ret2)