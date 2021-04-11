#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 9:41
# @Author     : john
# @File       : c01_10.py

class Open():
    def __enter__(self):
        print('open')

    def __exit__(self, type, value, trace):
        print('close')

    def __call__(self):
        print('Open call')
        pass


with Open() as f:
    pass
