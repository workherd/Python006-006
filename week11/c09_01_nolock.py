#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 7:58
# @Author     : john
# @File       : c09_01_nolock.py


import threading
import time

num = 0


def addon():
    global num
    num += 1
    time.sleep(1)  # 需休眠才能观察到脏数据
    print(f'num value is {num} \n')


for i in range(10):
    t = threading.Thread(target=addon)
    t.start()


print('主进程结束')