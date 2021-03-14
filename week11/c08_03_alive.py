#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 23:06
# @Author     : john
# @File       : c08_03_alive.py
import threading
import time


def start():
    time.sleep(5)


thread1 = threading.Thread(target=start)
print(thread1.is_alive())
thread1.start()
print(thread1.getName())
print(thread1.is_alive())

thread1.join()
print(thread1.is_alive())

