#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 15:46
# @Author     : john
# @File       : c14_05.py
# check iter
def check_iterator(obj):
    if hasattr(obj, '__iter__'):
        if hasattr(obj, '__next__'):
            print(f'{obj} is a iterator')
        else:
            print(f'{obj} is a iterable')
    else:
        print(f'{obj} can not iterable')


def func1():
    yield range(5)

check_iterator(func1)
check_iterator(func1())
