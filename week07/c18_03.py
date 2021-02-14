#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/14 10:48
# @Author     : john
# @File       : c18_03.py

# 进程池和协程

from multiprocessing import Pool
import asyncio
import time


async def test(time):  # 改成自己的程序就可以了
    await asyncio.sleep(time)


async def main(num):
    # print('222')
    start_time = time.time()
    # print('333')
    tasks = [asyncio.create_task(test(1)) for proxy in range(num)]
    [await t for t in tasks]
    print(time.time() - start_time)


def run(num):
    asyncio.run(main(num))


if __name__ == '__main__':
    start_time = time.time()
    p = Pool()
    for i in range(4):
        p.apply_async(run, args=(2500,))
    p.close()
    # print('111')
    p.join()
    print(f'total {time.time() - start_time}')
