#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 11:55
# @Author     : john
# @File       : c10.py

# functools.wraps
# @wraps 接受一个函数来进行装饰，同时加入了赋值函数名称、注释文档、参数列表等功能
# 装饰器里面可以访问在装饰之前的函数属性
# @functools.wraps(wrapped, assigned=WRAPPer_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 用于在定义包装函数时发起调用update_wrapper()作为函数装饰器
# 他等价于partial(update_wrappper, wrapped=wrappped, assigned=assigned, updated=updated)

from time import ctime,sleep
from functools import wraps
def outer_arg(bar):
    def outer(func):
        # 结构不变 增加wraps 可保持原来的名字不变
        @wraps(func)
        def inner(*args, **kwargs):
            print('%s called at %s'%(func.__name__, ctime()))
            ret = func(*args, **kwargs)
            print(bar)
            return ret
        return inner
    return outer


@outer_arg('foo_arg')
def foo(a,b,c):
    """  __doc__ """
    return (a+b+c)

print(foo.__name__)