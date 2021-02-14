#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:20
# @Author     : john
# @File       : c09.py

def outer(func):
    def inner(a, b):
        print(f'inner: {func.__name__}')
        print(a, b)
        func(a, b)
    return inner


@outer
def foo(a, b):
    print(a+b)
    print(f'foo: {foo.__name__}')
    print('******foo func')


foo(1, 2)
a = foo.__name__
print(a)