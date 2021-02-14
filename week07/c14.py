#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 15:19
# @Author     : john
# @File       : c14.py

def func():
    yield 0


print(type(func()))
func()