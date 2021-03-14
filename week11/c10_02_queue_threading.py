#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/14 8:47
# @Author     : john
# @File       : c10_02_queue_threading.py

import queue
import threading
import random
import time

writelock = threading.Lock()


class Producer(threading.Thread):
    def __init__(self, q, con, name):
        super(Producer, self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print(f'Producer {self.name} Started')

    def run(self):
        while 1:
            global writelock
            self.con.acquire()  # 获取锁

            if self.q.full():
                with writelock:
                    print('Queue is full, producer wait')
                self.con.wait()  # 等待资源

            else:
                value = random.randint(0, 10)
                with writelock:
                    print(f'{self.name} put value {self.name} {str(value)} in queue')
                self.q.put( (f'{self.name} : {str(value)}'))  # 放入队列
                self.con.notify()  # 通知消费者
                time.sleep(1)
        self.con.release()


class Consumer(threading.Thread):
    def __init__(self, q, con, name):
        super(Consumer, self).__init__()
        self.q = q
        self.name = name
        self.con = con
        print(f'Consumer {self.name} Started')

    def run(self):
        while 1:
            global writelock
            self.con.acquire()
            if self.q.empty():  # 队列空
                with writelock:
                    print('Queue is empty, consumer wait')
                self.con.wait()  # 等待资源

            else:
                value = self.q.get()
                with writelock:
                    print(f'{self.name} get value {value} from queue')
                self.con.notify()  # 通知生产者
                time.sleep(1)
        self.con.release()





if __name__ == '__main__':
    q = queue.Queue(10)
    con = threading.Condition()  # 条件锁

    p1 = Producer(q, con, 'P1')
    p1.start()
    p2 = Producer(q, con, 'P2')
    p2.start()
    c1 = Consumer(q, con, 'C1')
    c1.start()


# 联系使用列表实现队列

