#!/usr/bin/env python
# -*- coding:utf-8 -*-

gennumber = (i for i in range(0,2))
print(next(gennumber))
print(next(gennumber))

try:
    print(next(gennumber))

except StopIteration:
    print(StopIteration)
    print('最后一个元素')