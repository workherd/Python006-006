#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 21:57
# @Author     : john
# @File       : c07_timeout.py
from multiprocessing import Pool
import time


def f(x):
    return x*x


if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 进程池包含4个进程
        print(pool.map(f, range(10)))  # 输出‘[0, 1, 4, ... , 81]’
        it = pool.imap(f, range(10))  # 输出列表， imap输出迭代器
        print(it)
        print(next(it))
        print(next(it))
        print(next(it))
        print(next(it))
        print(it.next(timeout=1))

    print('主进程结束')