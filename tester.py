#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
#
# start_time = time.time()
# time.sleep(2)
# print(time.time() - start_time)


def func(name: str):
    print('函数收到变量的类型', type(name))
    print(name)

a = 122
print('a的类型为',type(a))
func(a)


