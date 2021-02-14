#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 12:59
# @Author     : john
# @File       : c11_03.py
# 装饰器 装饰类

def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)

        def display(self):
            # 将runtime()替换为display()
            self.times += 1
            print('run times ', self.times)
            self.wrapped.display()

    return newClass

@decorator
class MyClass(object):
    def __init__(self, number):
        self.number = number

    # 重写display
    def display(self):
        print('number is', self.number)


six = MyClass(6)
for i in range(5):
    six.display()

