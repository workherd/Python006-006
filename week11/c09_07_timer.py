#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:39
# @Author     : john
# @File       : c09_07_timer.py
# 定时器 指定n秒后执行

from threading import Timer


def hello():
    print('hello, world')


t = Timer(1,hello)
t.start()
print('主线程结束')