#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 23:32
# @Author     : john
# @File       : c18_server.py
# web Server
from aiohttp import web


# view
async def index(request):
    return web.Response(text='hello aiohttp')


# routes
def setup_routes(app):
    app.router.add_get('/', index)


# app
app = web.Application()
setup_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)  # 启动程序