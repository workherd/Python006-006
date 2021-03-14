#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 23:00
# @Author     : john
# @File       : c08_02_create_thread_by_class.py

import threading


class MyThread(threading.Thread):
    def __init__(self, n):  # 重构run函数必须要写
        super().__init__()
        self.n = n

    def run(self):
        print('current task:', self.n)


if __name__ == '__main__':
    t1 = MyThread("thread 1")
    t2 = MyThread("thread 2")

    t1.start()
    t2.start()
    # 将t1 t2 加到主线程
    t1.join()
    t2.join()
