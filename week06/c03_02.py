#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 20:52
# @Author     : john
# @File       : c03_02.py

class Kls2(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')


me = Kls2('john', 'li')
me.print_name()

# 输入若为 john-li
# 解决方法1： 修改__init__()
# 解决方法2： 增加__new__()  构造函数，有且仅有一个
# 解决方法3： 增加 提前处理的函数


def pre_name(obj, name):
    fname, lname = name.split('-')
    return obj(fname,lname)


me2 = pre_name(Kls2, 'john-li')
me2.print_name()


##################
class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def pre_name(cls, name):
        fname, lname = name.split('-')
        return cls(fname, lname)

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')


me3 = Kls3.pre_name('john-li')
me3.print_name()