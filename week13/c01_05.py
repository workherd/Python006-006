#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:16
# @Author     : john
# @File       : c01_03.py

try:
    1/0
except Exception as e:
    try:
        1/0
    except Exception as f:
        pass
    print(e)  # 输出异常

print('end ')
