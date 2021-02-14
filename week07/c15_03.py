#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 20:09
# @Author     : john
# @File       : c15_03.py
# 迭代器一旦耗尽，将永久损坏

x = iter([y for y in range(5)])
for i in x:
    print(i)
x.__next__()