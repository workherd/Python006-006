#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 12:31
# @Author     : john
# @File       : c06.py

def fun(*args, **kwargs): ## **kwargs优先获取
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


fun(123, 'zx', name='xvalue')

class kls(meta=type):
    pass
