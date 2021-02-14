#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 9:54
# @Author     : john
# @File       : c07.py

# 闭包,可以引用函数外的变量
def line_conf():
    b = 10

    def line(x):
        return 2*x+b
    return line  # 返回对象


b = -1
my_line = line_conf()
print(my_line(5))

# 这样出处理的意义：调用简单

# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)