#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:12
# @Author     : john
# @File       : c01_02.py


def a():
    return b()


def b():
    return c()


def c():
    return d()


def d():
    x = 0
    return 100/x


a()