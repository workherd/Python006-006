#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 12:41
# @Author     : john
# @File       : c06_lock.py

# 加进程锁
# 为了解决不同进程抢共享资源的问题，我们可以用加进程锁来解决。
import multiprocessing as mp
import time


def job(v, num, l):
    l.acquire()  # 锁住  开始操作的时候就要加锁
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value, end='|')
    l.release()  # 释放


def multicore():
    l = mp.Lock()  # 定义一个进程所,
    v = mp.Value('i', 0)  # 定义共享内存
    # 进程所的信息传入多个进程中
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    multicore()

# 在某些特定的场景下要共享string类型，方式如下：
# from ctypes import c_char_p
# str_val = mp.Value(c_char_p, b"Hello World")