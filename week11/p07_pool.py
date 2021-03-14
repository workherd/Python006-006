#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 13:31
# @Author     : john
# @File       : p07_pool.py
# pool类表示一个工作晋城市
# 如要启动大量的子进程，可用进程池的方式批量创建子进程

from multiprocessing.pool import Pool
from time import sleep, time
import random, os


def run(name):
    print('%s 子进程开始，进程ID：%d' % (name, os.getpid()))
    start = time()
    sleep(random.choice([3, 4, 5, 6]))
    end = time()
    print("%s 子进程结束，进程id：%d, 耗时%0.2f" % (name, os.getpid(), end-start))


if __name__ == '__main__':
    print('父进程开始')
    # 创建多个进程， 表示可以同时执行的进程梳理。默认大小是cpu的核心数
    p = Pool(4)
    for i in range(10):
        # 创建进程，放入进程池统一管理
        p.apply_async(run, args=(i, ))  # 异步方式
        # p.apply(run, args=(i, ))  # 同步方式，同for循环，无意义
    # 若使用进程池，在调用join（）之前必须要先clase()
    # 且在close（）之后不能再继续往进程池添加新的集成
    p.close()
    # 进程池调用join，会等待进程中所有的子进程结束完毕再去结束父进程
    p.join()
    print('父进程结束。')
    p.terminate()

# close()：如果我们用的是进程池，在调用join()之前必须要先close()，
# 并且在close()之后不能再继续往进程池添加新的进程
# join()：进程池对象调用join，会等待进程池中所有的子进程结束完毕再去结束父进程
# terminate()：一旦运行到此步，不管任务是否完成，立即终止。
