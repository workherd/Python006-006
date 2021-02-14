#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 12:53
# @Author     : john
# @File       : c11_02.py
# 类装饰器
class Count(object):
    def __init__(self, func):
        self._func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):  # 模拟成函数，将类模拟成可调用的对象
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')


@Count
def example():
    print('hello')


example()
print(type(example))
example()
example()



