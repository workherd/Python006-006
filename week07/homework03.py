#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/14 11:34
# @Author     : john
# @File       : homework03.py
"""
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""

import time
from functools import wraps


def time_checker(func):
    @wraps(func)
    def inner(*args, **kwargs):
        time_start = time.time()
        ret = func(*args, **kwargs)
        print(f'{func.__name__} running time is {time.time() - time_start} 秒')
        return ret
    return inner


@time_checker
def func1():
    time.sleep(1)
    print(f'now func1 is  running')


if __name__ == '__main__':
    func1()



