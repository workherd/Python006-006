#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:38
# @Author     : john
# @File       : c01_09.py

# file1 = open('a.txt', encoding='utf8')
# try:
#     data = file1.read()
# finally:
#     file1.close()

with open('a.txt', encoding='utf9') as file2:
    data = file2.read()

print('end')