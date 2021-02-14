#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 23:14
# @Author     : john
# @File       : c17_02.py

import asyncio


async def main():
    print('hello')
    await asyncio.sleep(3)  # sleep 3s
    print('world')

# async.io.run()运行最高级别的conroutine
asyncio.run(main())

# 协程调用过程
# 调用协程时，会注册到ioloop，返回coroutine对象，用ensure_future封装为Future对象，提交给ioloop