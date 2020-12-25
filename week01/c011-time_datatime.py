#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from datetime import datetime,timedelta

a = time.time()
print('时间戳')
print(a)
print('localtime()')
print(time.localtime())
print('时间的格式化')
aa = time.strftime('%Y-%m-%d %X',time.localtime())
print(aa)
print('字符转换为时间对象')
print(time.strptime('2020-12-22 16:43:01','%Y-%m-%d %X'))

print('*'*11,'datatime 时间偏移的处理','*'*11)
print('now()')
print(datetime.now())
print('today()')
print(datetime.today())
print('时间偏移')
print("day+1")
print(datetime.today() - timedelta(days=1))
print(datetime.today() + timedelta(days=-1))


a = time.ctime()
print(a)