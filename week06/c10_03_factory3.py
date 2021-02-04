#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 20:47
# @Author     : john
# @File       : c10_02_factory2.py

# 返回在函数内动态创建的类 
def factory2(func):
    class klass: pass
    # setattr 需要三个参数：对象、key、value
    print(func)
    setattr(klass, func.__name__, classmethod(func))
    return klass


def say_foo(self):
    print('bar')


Foo = factory2(say_foo)
Foo.say_foo()
# foo = Foo()
# foo.say_foo()
