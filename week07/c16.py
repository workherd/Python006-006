#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 20:12
# @Author     : john
# @File       : c16.py
# yield 做输入输出

def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index  # 可以将程序从yield处分割为两部分
        print(f'jump is {jump}')
        if jump is None:
            jump = 1  # next() 或 send（none）
        index += jump
        print(f'index is {index}')


if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator))  # 0
    print(iterator.send(2)) # 2
    print(next(iterator))  # 3 # next = send(none)
    print(iterator.send(-1))  # 2
    print('*'*88)
    for x in iterator:
        print(x)


# yield 可以形成协程