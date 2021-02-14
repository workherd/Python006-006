#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:41
# @Author     : john
# @File       : c09_04.py

# 装饰器带参数

def outer_arg(bar):
    def outer(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(bar)
            return ret
        return inner
    return outer

# 相当于 outer_arg('foo_arg')(foo)()


@outer_arg('foo_arg')
def foo(a, b, c):
    return (a+b+c)


print(foo(1,3,5))