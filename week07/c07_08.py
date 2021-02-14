#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 10:34
# @Author     : john
# @File       : c07_08.py

# nonlocal 访问外部函数的局部变量
# 注意start的位置， return的作用域和函数内的作用域不同


def counter2(start=2):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr


c1 = counter2(5)
print(c1())
print(c1())

c2 = counter2(50)
print(c2())
print(c2())
print(c2())

print(c1())
print(c1())
print(c1())


print(c2())
print(c2())
