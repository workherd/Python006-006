#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 21:08
# @Author     : john
# @File       : c03_03.py

class Fruit(object):
    total = 0
    # 对象在引用classmethod的时候，自己的dict没有，他会找自己实例对应的类，在没有就会寻找类的父类

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls} , {value}')
        cls.total = value


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass


print('apple set 100')
Apple.set(100)
print('orange set 200')
Orange.set(200)
print('orange()')
org = Orange()  # 实例化
print(org.print_total())
print('org_set300')
org.set(300)

print('apple print total')
Apple.print_total()
