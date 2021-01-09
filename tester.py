#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib

a = '你好'
def my_urlencode(str):
    reprStr = repr(str).replace(r'\x', '%')
    return reprStr[1:-1]


print( my_urlencode('你好'))

print(urllib.parse.urlencode(a))

