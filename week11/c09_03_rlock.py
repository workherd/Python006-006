#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:09
# @Author     : john
# @File       : c09_03_rlock.py

import threading
import time

# Lock 普通锁不可以嵌套， RLock可以嵌套

mutex = threading.RLock()


class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire(1):
            print(f'thread {self.name} get mutex')
            time.sleep(1)
            mutex.acquire()
            mutex.release()
        mutex.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()