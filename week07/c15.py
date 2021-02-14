#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 19:50
# @Author     : john
# @File       : c15.py
import itertools

# 无限迭代计数
count = itertools.count()

next(count)
print(count)
next(count)
print(count)
next(count)
print(count)

# 迭代器实现了迭代器协议，通过next方式可以进行调用

cycle = itertools.cycle(('yes', 'no'))  # 无限循环遍历
a = next(cycle)
print(a)
a = next(cycle)
print(a)
a = next(cycle)
print(a)


repeat = itertools.repeat(10, times=2)  # 重复
a = next(repeat)
print(a)
a = next(repeat)
print(a)
# next(repeat)


# 有限迭代器
for j in itertools.chain('ABC', [1, 2, 3]):
    print(j)


# yield from  -- py3.3以后

def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = 'ABC'
t = [1, 2, 3]
a = list(chain(s,t))
print(a)


def chain2(*iterables):
    for i in iterables:
        yield from i


a = list(chain2(s,t))
print(a)

