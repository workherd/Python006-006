#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:42
# @Author     : john
# @File       : c10_01_queue.py

import queue

q = queue.Queue(5)  # 大小为5
q.put(111)
q.put(222)
q.put(333)

print(q.get())
print(q.get())
q.task_done()  # 处理好数据库后执行，提示q.join()是否停止阻塞，让线程继续执行或退出

print(q.qsize())  # 队列的大小
print(q.empty())  # 队列是否为空
print(q.full())  # 队列是否满了

