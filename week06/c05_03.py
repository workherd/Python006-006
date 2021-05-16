#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 19:01
# @Author     : john
# @File       : c.py
class Human2(object):
    """ getattribute对任意属性进行截获"""

    def __init__(self):
        self.age = 18

    def __getattribute__(self, item):
        print(f'__getattribute___ call item:{item}')
        return super().__getattribute__(item)  # supper表示当前类的父类
        # return self.__getattribute__(item)


h1 = Human2()
print(h1.age)
# print(h1.noattr)
print('end')
