#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 14:33
# @Author     : john
# @File       : c13_03.py

import math
print('The value of Pi is approximately %5.3f.' % math.pi)  ## 原始输出

print('{1} and {0}'.format('spam', 'eggs'))  # 位置描述

print('The story of {0}, {1}, and {other}'.format('bill', 'manfred', other='Georg'))  # 关键词描述

firsname = 'li'
lastname = 'john'
print('hello, %s %s' % (lastname, firsname))
print('hello, {1} {0}'.format(firsname,lastname))
print(f'hello, {lastname} {firsname}, {2*5}')

