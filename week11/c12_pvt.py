#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 9:54
# @Author     : john
# @File       : c12_pvt.py
import multiprocessing as mp
import time

def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res)  # queue

# 多核
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore', res1+res2)


# 创建多线程multithread
import threading as td


def multithread():
    q = mp.Queue()
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('mutithread:', res1+res2)


#创建普通函数
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal', res)


if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:',st1-st)
    st = time.time()
    multithread()
    st1 = time.time()
    print('multithread time:', st1-st)
    st = time.time()
    multicore()
    print('multicore time:', time.time()-st)

