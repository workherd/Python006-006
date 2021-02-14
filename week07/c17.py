#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 20:52
# @Author     : john
# @File       : c17.py
# py3.4 支持事件循环的方法

import asyncio


@asyncio.coroutine
def py34_func():
    yield from sth()


# py 3.5 增加async await

async def py35_func():
    await sth()