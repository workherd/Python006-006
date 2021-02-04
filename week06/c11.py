#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 21:06
# @Author     : john
# @File       : c11.py
# 使用type元类创建类

def hi():
    print('Hi metaclass')


# type的三个参数：类名、父类的元组、类的成员
Foo = type('Foo', (), {'say_hi':hi})
foo = Foo
foo.say_hi()
print(type(Foo))
print(type(foo))
# 元类type首先是一个类，所以比类工厂的方法更灵活多变，可以自由创建子类来扩展元类的能力