#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 18:46
# @Author     : john
# @File       : c04_02.py

class Foo(object):
    """ 类的三种语法"""

    def instance_methon(self):
        print('类的示例方法，只能被示例对象调用')

    @staticmethod
    def static_method():
        print('是静态方法')

    @classmethod
    def class_method(cls):
        print('类的方法')

foo = Foo()

foo.instance_methon()
foo.static_method()
foo.class_method()
print('-'* 88)
Foo.static_method()
Foo.class_method()
# Foo.instance_methon()