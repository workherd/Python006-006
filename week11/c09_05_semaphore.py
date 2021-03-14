#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:25
# @Author     : john
# @File       : c09_05_semaphore.py

import time, threading


def run(n):
    semaphore.acquire()
    print("run the thread : %s \n" % n)
    time.sleep(2)
    semaphore.release()


num = 0

semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行

for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()