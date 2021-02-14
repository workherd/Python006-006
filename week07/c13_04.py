#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 14:41
# @Author     : john
# @File       : c13_04.py
# typeing 类型注解（type hint）， 只是提示

def func(text: str, number: int) -> str:
    return text * number


a = func('a', 5)
print(a)