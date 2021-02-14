#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 12:30
# @Author     : john
# @File       : c10_03.py

import functools


@functools.lru_cache()   # lru_cache(maxsize=123, typed=False) 有两个可选参数，maxsize代表换成的内存占有值，超过此值后就会被释放， # typed=true, 则会把不同的参数类型得到的结果分开保存
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("fibonacci(6)", setup="from __main__ import fibonacci"))