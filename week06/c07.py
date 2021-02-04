#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/28 18:10
# @Author     : john
# @File       : c07.py
# __getattribute__的底层原理是描述器

class Desc(object):
    """
    通过打印来展示描述器的访问流程
    """
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f'__get__{instance} {owner}')  # instance 表示当前类   owner 属于的类
        return self.name

    def __set__(self, instance, value):
        print(f'__set__{instance} {value}')
        self.name = value

    def __delete__(self, instance):
        print(f'__delete__{instance}')
        del self.name

class MyObj(object):
    a = Desc('aaa')
    b = Desc('bbb')


print('开始实例化')
my_object = MyObj()
print('结束实例化')
print(my_object.a)
my_object.a = 456
print(my_object.a)