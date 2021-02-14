#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 9:54
# @Author     : john
# @File       : c07.py

# 闭包
def line_conf():
    def line(x):
        return 2*x+1
    return line  # 返回对象


my_line = line_conf()
print(my_line(5))

# 这样出处理的意义：调用简单