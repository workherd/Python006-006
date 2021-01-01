#!/bin/python3
# -*- coding: utf-8 -*-
import time
from queue import Queue
import threading
q = Queue(20)
q1 = Queue(20)
for i in range(20):
    q.put(i)


def de(i):
    '''生产者'''
    print(f'生产者线程{i}开始')
    while not q.empty():
        try:
            time.sleep(2)
            data = q.get_nowait()

            print(f'生产 {data}')
            q1.put(data)
            q.task_done()
        except Exception as e:
            pass
    print(f'生产者线程{i}结束')


def da(i):
    '''消费者'''
    print(f'消费者线程{i}开始')
    while True:
        try:
            time.sleep(5)
            data = q1.get_nowait()
            print(f'消费 {data}')
            q1.task_done()
        except Exception as e:
            pass
    # flg=False
    # print(f'消费者线程{i}结束')


for i in range(3):
    thread = threading.Thread(target=de, args=(i, ))
    # 设定他为守护进程，一旦任务完成，主线程结束，子线程立马结束
    thread1 = threading.Thread(target=da, args=(i, ), daemon=True)
    thread.start()
    thread1.start()
q.join()
print(f'q1还有{q1.unfinished_tasks}任务没完成')
q1.join()
print('主线程结束')