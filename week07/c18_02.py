#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 23:48
# @Author     : john
# @File       : c18_client.py

import aiohttp  # http层面的处理
import asyncio  # 处理注册问题get_event_loop

urls = [
    'http://httpbin.org',
    'http://httpbin.org/get',
    'http://httpbin.org/ip',
    'http://httpbin.org/headers'
]


async def crawler():
    async with aiohttp.ClientSession() as session:
        futures = map(asyncio.ensure_future, map(session.get, urls))
        for task in asyncio.as_completed(futures):
            print(await task)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.ensure_future(crawler()))
