#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 12:22
# @Author     : john
# @File       : c05_03.py

# prog1 同名不同作用域的问题
x = 1


def func():
    x = 2

func()
print(x)

# 查找顺序
y = 2
def fun2():
    print(y)
fun2()

# # prog3 err
#
# def func3():
#     z = 3
# func3()
# print(z)


# prog4 err
def func4():
    print(a)
func4()
a = 100
