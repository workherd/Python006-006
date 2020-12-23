#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import deque

str1 = 'abc'
# help(deque)

atog = deque('def')
print(atog)

atog.append('g')
print(atog)

atog.appendleft('c')
print(atog)

atog.extendleft('ba')
print(atog)

print('*'*88)

for i in atog:
    print(i)