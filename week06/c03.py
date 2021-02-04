#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 19:20
# @Author     : john
# @File       : c03.py

# 让实例的方法成为类的方法
class Kls1(object):
    bar = 1

    def foo(self):
        print('in foo')

    # 使用类属性、方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()


Kls1.class_foo()


# import django
##############
class Story(object):
    snake = 'python'

    # __new__() 是python构造函数
    def __init__(self, name):  # 初始化函数，类实例化的时候，此函数默认引用；参数第一个self，后面是类可以接收的参数
        self.name = name

    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake  # 好处：类Story引用get_apple_to_eve的时候，cls会自动变成story，会变成story.snake


s = Story('anyone')
print(s.get_apple_to_eve)  # bound方法，查找顺序是先找s的__dict__是否有get_apple_to_eve,如果没有，查类story
print(s.get_apple_to_eve())  # 实例可以使用
print(Story.get_apple_to_eve())  # 类也可以使用