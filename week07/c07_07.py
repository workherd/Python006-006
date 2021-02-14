#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 10:29
# @Author     : john
# @File       : c07_07.py

# 内部函数对外部函数作用域里面变量的调用（非全局变量），称内部函数函数为闭包

def counter(start=0):
    count = [start]

    def incr():
        count[0] += 1
        return count[0]
    return incr


c1 = counter(10)
print(c1())
print(c1())
print(c1())
print(c1())


