#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 10:27
# @Author     : john
# @File       : c03_02.py

# import collections

# 命名元组
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y=20)

print(p.x+p.y)
print(p[0]+p[1])
x,y = p
print(x)
print(y)

from collections import Counter
mystring = ['a','b','c','d','d','d','e','e','c','c','c']
cnt = Counter(mystring)
print(cnt.most_common(3))
print(cnt['b'])

#双向队列
from collections import deque
d = deque('uvw')
d.append('xyz')
d.appendleft('rst')
print(d)