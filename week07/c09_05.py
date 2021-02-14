#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:49
# @Author     : john
# @File       : c09_05.py
# 装饰器堆叠，注意装饰器的顺序是有要求的，可能会影响执行结果

@classmethod
@syncronized(lock)
def foo(cls):
    pass


def foo(cls):
    pass

foo2 = syncronized(lock)(foo)
foo3 = classmethod(foo2)
foo = foo3
