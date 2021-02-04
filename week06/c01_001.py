#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 15:12
# @Author     : john
# @File       : c01_001.py

class MyFirstClass:
    pass


a = MyFirstClass()
b = MyFirstClass()

# 不同内存地址，两个不同对象
print('a type',type(a))
print('b type',type(b))

print('id a ', id(a), 'id b', id(b))
print('a_class', a.__class__(), 'b_class', b.__class__())

# 类也是对象
c = MyFirstClass
d = c()
print('d_class', d.__class__())