#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 23:48
# @Author     : john
# @File       : c18_client.py

import aiohttp  # http层面的处理
import asyncio  # 处理注册问题get_event_loop

url = 'http://httpbin.org/get'


async def fetch(client, url):
    # get 方式请求url
    async with client.get(url) as resp:
        assert resp.status == 200
        return await resp.text()


async def main():
    # 获取session对象
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, url)
        print(html)

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)  # 程序运行
# Zero-sleep 让底层连接得到关闭的缓冲时间
loop.run_until_complete(asyncio.sleep(0))
loop.close()

