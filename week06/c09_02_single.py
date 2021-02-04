#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 19:56
# @Author     : john
# @File       : c09_01_single.py
# 装饰器实现单实例模式
class Foo(object):
    def __new__(cls, name):
        print('trace__new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('trace__init__')
        super().__init__()
        self.name = name


bar = Foo('test')
print(bar.name)


# 使用new完成单实例
class Singleton2(object):
    __isinstance = False  # 默认没有被实例化

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.__isinstance  # 返回实例化对象
        cls.__isinstance = object.__new__(cls)  # 实例化
        return cls.__isinstance


# 单实例用在多线程的时候就要做加锁的事情
class _Singleton(object):
    pass


Singleton = _Singleton()
del _Singleton
another = Singleton.__class__()

