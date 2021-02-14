#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 15:23
# @Author     : john
# @File       : c14_02.py


print([i for i in range(0,11)])
print((i for i in range(0,11)))
gennumber = (i for i in range(0,11))
print(f' {gennumber}  {next(gennumber)}  {next(gennumber)}  {next(gennumber)} ')  # gennumber.__next__() 与next（gennumber）功能相同
# 生成器实现了完成的迭代器协议
for i in gennumber:
    print(i)
next(gennumber)