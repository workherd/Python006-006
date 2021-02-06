#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/5 23:16
# @Author     : john
# @File       : c01.py

# question 1
print('__question1__'*11)
a = 123
b = 123
c = a
c is a  # 后台比较的是内存地址是否相等

print(id(a))
print(id(b))
print(id(c))

print('__question2__'*11)
a = 456
print(id(a))
c = 789
c = b = a
print(a)
print(b)
print(c)

print('__question3__'*11)
x = [1, 2, 3]
y = x
x.append(4)
print(x)
print(y)
print('__question4__'*11)
a = [1, 2, 3]
b = a
a = [4, 5, 6]
print(a)
print(b)

print('__question5__'*11)
a = [1, 2, 3]
b = a
a[0], a[1], a[2] = 4, 5, 6
print(a)
print(b)