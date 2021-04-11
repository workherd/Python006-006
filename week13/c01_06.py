#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:21
# @Author     : john
# @File       : c01_06.py


def f1():
    1/0


def f2():
    list1 = []
    list1[1]
    f1()


def f3():
    f2()


try:
    f3()
except (ZeroDivisionError, Exception) as e:
    print(e)