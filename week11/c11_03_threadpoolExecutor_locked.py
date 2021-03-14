#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 9:38
# @Author     : john
# @File       : c11_02_threadpoolExecutor.py

from concurrent.futures import ThreadPoolExecutor   #  方便的使用多线程多进程
import time


def wait_on_b():
    time.sleep(5)
    print(b.result())  #
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())
    return 6


executer = ThreadPoolExecutor(max_workers=2)
a = executer.submit(wait_on_b)
b = executer.submit(wait_on_a)

# 当回调已关联了一个 Future 然后再等待另一个 Future 的结果时就会发产死锁情况
# https://docs.python.org/zh-cn/3.7/library/concurrent.futures.html#threadpoolexecutor

