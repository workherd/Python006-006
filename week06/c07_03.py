#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/28 18:24
# @Author     : john
# @File       : c07_02.py

class Human2(object):
    def __init__(self):
        self._gender = None

    # 将方法封装成属性 # 方法调用 #
    @property
    def gender2(self):
        print(self._gender)

    # 支持修改
    @gender2.setter
    def gender2(self, value):
        self._gender = value

    # 支持删除
    @gender2.deleter
    def gender2(self):
        del self._gender


h = Human2()
h.gender = 'F'
print(h.gender)
del h.gender

# property的另一种写法
# gender = property(get_, set_, del_, 'other property')

# 被装饰的函数，建议使用相同的函数名称
# 使用setter 并不能真正意义上实现无法写入，gender被改名为 _Article__gender

# property 本质不是函数， 而是特殊类（实现了数据描述符的类）
# 若一个对象同时定义了__get__（）和__set__() 方法，则成为数据描述符
# 若仅定义了__get__()方法，则成为非数据描述符

# property的有点：
# 代码简洁，可读性可维护性强
# 实现了属性可管理
# 控制属性访问权限，提高数据安全性
