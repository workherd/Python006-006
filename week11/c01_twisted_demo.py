#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 8:26
# @Author     : john
# @File       : twisted_demo.py

from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor


def response(*args, **kwargs):
    # print(args, kwargs)
    print('返回的网页内容')


def callback(*args):
    print('执行了一个回调', args)


@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode('utf-8'))
    d.addCallback(response)
    d.addCallback(callback)
    yield d


def stop(*args, **kwargs):
    reactor.stop()


urls = ['https://www.baidu.com', 'http://www.sougou.com']
li = []

for url in urls:
    ret = start(url)
    li.append(ret)
print(li)
print('*'*88)

d = defer.DeferredList(li)
d.addBoth(stop)
reactor.run()
