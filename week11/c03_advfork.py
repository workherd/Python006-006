#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 10:55
# @Author     : john
# @File       : c03_advfork.py

import time
from multiprocessing import Process
import os


def run():
    print('子进程开启')
    time.sleep(2)
    print('子进程结束')


if __name__ == '__main__':
    print('父进程开启')
    p = Process(target=run)
    p.start()
    p.join()
    print('父进程结束')

