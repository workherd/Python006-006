#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 12:12
# @Author     : john
# @File       : c10_02.py
# flask 案例
from functools import wraps

def requires_auth(func):
    @wraps(func)
    def auth_method(*args, **kwargs):
        if not auth:
            authenticate()
        return func(*args, **kwargs)
    return auth_method

@requires_auth
def func_demo():
    pass


from functools import wraps


def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_functions(*args, **kwargs):  # 需要真实的函数名字才可以,若没有warps 就会发现都是内部名字
            log_string = func.__name__ + ' was called'
            print(log_string)
            with open(logfile, 'a') as opend_files:
                opend_files.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_functions
    return logging_decorator


@logit
def myfunc1():
    pass

myfunc1()
# Output: myfucn1 was called

@logit(logfile='func2.log')
def myfunc2():
    pass


#  原来的包
# 可使用wrapt包替代@wraps

import wrapt
def with_arguments(myarg1, myarg2):
    @wrapt.decoratror
    def wrapper(wrapped, instances, args, kwargs):
        return wrapped(*args, **kwargs)
    return wrapper

@with_arguments(1,2)
def functions():
    pass
