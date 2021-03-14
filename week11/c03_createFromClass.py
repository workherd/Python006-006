#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 11:24
# @Author     : john
# @File       : c03_createFromClass.py
# multiprocessing.Process的run()方法
import os, time
from multiprocessing import Process


class NewProcess(Process):  # 继承process类创建一个新类
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):  # 重写Process类中的run方法
        while True:
            print(f'我是进程:{self.num}, 我的pid是：{os.getpid()}')
            time.sleep(1)


for i in range(2):
    p = NewProcess(i)
    p.start()

# 当不给Process指定target时，会默认调用Process类里的run()方法。
# 这和指定target效果是一样的，只是将函数封装进类之后便于理解和调用。

