#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:14
# @Author     : john
# @File       : c09_04_conditions_waite_lock.py

# 条件锁： 使线程等待，只有满足条件时，才释放n个线程

import threading


def condition():
    ret = False
    r = input(">>>>")
    if r == 'yes':
        ret = True
    return ret


def func(conn, i):
    # print i
    conn.acquire()
    conn.wait_for(condition)
    print(i+100)
    conn.release()


c = threading.Condition()
for i in range(10):
    t = threading.Thread(target=func, args=(c,i,))
    t.start()

# 条件锁的原理跟设计模式中的生产者／消费者（Producer/Consumer）模式类似
