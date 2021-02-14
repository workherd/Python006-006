#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 15:37
# @Author     : john
# @File       : c14_04.py

# 类实现完成的迭代器协议

class SampleIterator:
    def __iter__(self):
        return self

    def __next__(self):
        # 非结尾
        if ...:
            return ...
        else:
            raise StopIteration

# 函数事项完成的迭代器协议
def SampleGenerator():
    yield ...
    yield ...
    yield ...
    yield ...
    # 只要有yield 关键词，则此函数将不再是一个函数，而被称为‘生成器构造函数’，调用时就会产生一个生成器对象


