#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 9:38
# @Author     : john
# @File       : c11_02_threadpoolExecutor.py

from concurrent.futures import ThreadPoolExecutor   #  方便的使用多线程多进程
import time


def func(args):
    print(f'call func {args}')


if __name__ == '__main__':
    seed = ['a', 'b', 'c', 'd']

    with ThreadPoolExecutor(3) as executor:
        executor.submit(func, seed)  # 原样传递参数

    time.sleep(1)

    with ThreadPoolExecutor(3) as executor2:
        executor2.map(func, seed)  # 映射后传递

    time.sleep(1)

    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 2, 3)
        print(future.result())