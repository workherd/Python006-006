#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 10:04
# @Author     : john
# @File       : c07_04.py


def func():
    pass


func_magic = dir(func)
print(func_magic)  # 查看函数的属性


class ClassA(object):
    pass


obj = ClassA()
obj_magic = dir(obj)
print(obj_magic)  # 查看对象的默认属性

a = set(func_magic) - set(obj_magic)
print(a)  # 比较默认属性
