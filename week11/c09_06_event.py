#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:29
# @Author     : john
# @File       : c09_06_event.py

# 定义一个flag  ，设置flag为true  clear设置为false

import threading


def func(e,i):
    print( '\n', i)
    e.wait()  # 检测当前event是什么状态，如红灯则阻塞 如绿地则继续向下执行
    print(i+100, '\n')


if __name__ == '__main__':

    event = threading.Event()
    for i in range(10):
        t = threading.Thread(target=func, args=(event,i))
        t.start()

    event.clear()  # 主动将状态设置为红灯
    inp = input('>>>>')
    if inp == '1':
        event.set()  # 主动设置状态为绿灯

    print('主线程结束')

# 练习： 使用redis实现分布式锁

