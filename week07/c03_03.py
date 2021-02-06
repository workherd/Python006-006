#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 10:35
# @Author     : john
# @File       : c03_03.py

# 计算欧式距离

import numpy as np
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

op1 = np.sqrt(np.sum(np.square(vector1 - vector2)))
op2 = np.linalg.norm(vector1 - vector2)
print(op1)
print(op2)

from collections import namedtuple
from math import sqrt
Point = namedtuple('Point', ['x', 'y', 'z'])


class Vector(Point):
    def __init__(self, p1, p2, p3):
        super(Vector).__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __sub__(self, other):  # 实现运算符重载
        tmp = (self.p1 - other.p1)**2 + (self.p2 - other.p2)**2 + (self.p3 - other.p3)**2
        return sqrt(tmp)

# a - b  =====  a.__sub__(b)


p1 = Vector(1, 2, 3)
p2 = Vector(4, 5, 6)
print(p1-p2)