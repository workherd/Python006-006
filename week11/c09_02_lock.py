#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 7:58
# @Author     : john
# @File       : c09_01_nolock.py


import threading
import time

num = 0
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):  # 加锁
            num += 1
            print(f'{self.name}  : num value is  {num}')
        mutex.release()  # 解锁


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()

    print('主进程结束')