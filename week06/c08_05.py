#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 19:38
# @Author     : john
# @File       : c08_05.py

class Klass(object):
    def A(self):
        pass

    def A(self, a, b):
        print(f'{a},{b}')


inst = Klass()
# 没有实现重载
inst.A()  # 此时执行报错了
