#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/28 19:42
# @Author     : john
# @File       : c08.py
class People(object):
    def __init__(self, name):
        self.gene = 'XY'
        self.name = name

    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self, name):
        super().__init__(name)  # 找到man的父类，将people的对象转换为类man的对象

    def work(self):
        print('work hard')

class Woman(People):
    def __init__(self, name):
        super().__init__(name)

    def shopping(self):
        print('buy buy buy')


p1 = Man('Adam')
p2 = Woman('Eve')

# gene 是否有继承 # 没有继承 初始化函数覆盖了
print(p1.gene)

print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# type 元类由type自身创建， object类有元类type创建，type继承了object类

# 多个父类
class Son(Man, Woman):
    pass

# 继承顺序