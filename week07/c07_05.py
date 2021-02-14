#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 9:54
# @Author     : john
# @File       : c07.py

# 闭包,可以引用函数外的变量
def line_conf(a, b):  # 定义态

    def line(x):
        return a*x+b
    return line  # 返回对象


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))  # 运行态 # 实现了外部函数与内部函数的解耦；定义时做好了规则的设置，引用的时候不用考虑模式，
