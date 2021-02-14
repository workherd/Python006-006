#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 10:54
# @Author     : john
# @File       : c08_02.py

def decorate(func):  # 装饰器会在模块导入的时候自动运行
    print('running in module')

    def inner():
        return func()
    return inner


@decorate
def func2():
    pass

