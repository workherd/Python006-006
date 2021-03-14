#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 21:57
# @Author     : john
# @File       : c07_timeout.py
from multiprocessing import Pool
import time


def f(x):
    return x*x


if __name__ == '__main__':
    with Pool(processes=4) as pool:  # 进程池包含4个进程
        result = pool.apply_async(f, (10,))  # 执行一个子进程
        print(result.get(timeout=1))  # 显示执行结果

        result = pool.apply_async(time.sleep, (10,))
        print(result.get(timeout=1))  # raise  multiprocessing.TimeoutError  # 程序延时10秒 只等待1秒

    print('主进程结束')