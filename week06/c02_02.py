#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 16:48
# @Author     : john
# @File       : c02_02.py

class Human2(object):
    # 人为约定，不可修改
    _age = 0

    # 私有属性,防止被滥用和修改
    __fly = False

    # 魔术方法，不会自动改名
    # 如 __init__


# 自动改名机制
a = Human2.__dict__
print(a)
