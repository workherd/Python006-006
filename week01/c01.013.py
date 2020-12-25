#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
a = os.path.abspath('test.log')
print(a)

print('*'*88)
path = 'D:\peikangfiles\python\geektime\code\week01\test.log'
aa = os.path.basename(path)
print(aa)
print(os.path.dirname(path))
os.path.exists('/etc/passwd')  # 先检查后在处理文件
os.path.isfile('/etc/passwd')
os.path.isdir('/etc/passwd')
aa = os.path.join('a','b')
print(aa)

# test
aa = os.path.join('/a','b')
print(aa)

