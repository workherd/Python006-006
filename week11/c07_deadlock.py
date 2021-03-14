#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 21:11
# @Author     : john
# @File       : c07_deadlock.py
from multiprocessing import Process, Queue


def f(q):
    q.put('X'*3000000)


if __name__ == '__main__':
    queue = Queue()
    p = Process(target=f, args=(queue, ))
    p.start()
    p.join()  # 死锁
    obj = queue.get()
#  交换最后两行可以修复这个问题（或者直接删掉 p.join()）