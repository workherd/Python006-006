#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 12:40
# @Author     : john
# @File       : c11.py
# python 2.6 开始添加类装饰器

from functools import wraps

class MyClass(object):
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super(MyClass, self).__init__(*args, **kwargs)

    def __call__(self,func):  #call 来保证可以被调用
        # 类的装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + '   was called'
            print(func_name)
            return func(*args, **kwargs)
        return wrapped_function


def myfunc():
    pass


MyClass(100)(myfunc)()