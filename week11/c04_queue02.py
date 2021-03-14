#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 11:59
# @Author     : john
# @File       : c04_queue02.py.py
from multiprocessing import Process, Queue
import os, time


def write(q):
    print('启动Write子进程 %s' % os.getpid())
    for i in ['A', 'B', 'C', 'D']:
        q.put(i)  # 写入队列
        time.sleep(1)
    print('结束write子进程： %s' % os.getpid())


def read(q):
    print('启动Read子进程：%s' % os.getpid())
    while True:  # 阻塞， 等待获取write的值
        value = q.get(True)
        print(value)
    print('结束Read子进程：%s' % os.getpid())  # 不会执行


if __name__ == '__main__':
    # 父进程创建队列， 并传递给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()

    pw.join()
    # pr进入死循环 （写进程结束了，所以读进程也可以结束了）
    pr.terminate()  # 强制结束，读取时代码是允许的
    print('父进程结束')