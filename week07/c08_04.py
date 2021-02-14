#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:13
# @Author     : john
# @File       : c08_04.py
# 包装
def html(func):
    def decorator():
        return f'<html>{func()}</html>'
    return decorator

def body(func):
    def decorator():
        return f'<body>{func()}</body>'
    return decorator

@html
@body
def content():
    return 'hello world'


a = content()
print(a)
