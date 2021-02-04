#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 21:42
# @Author     : john
# @File       : c12_03.py

def mixin(klass, MixinKlass):
    klass.__bases__ = (MixinKlass,) + klass.__bases__


class Fclass(object):
    def text(self):
        print('in FatherClass')


class S1class(Fclass):
    pass


class MixinClass(object):
    def text(self):
        return super().text()
        print('in MixinClass')


class S2class(S1class, MixinClass):
    pass


print(f'test1: S1class MRO: {S1class.mro()}')
s1 = S1class()
s1.text()

mixin(S1class, MixinClass)
print(f'test2: S1class MRO: {S1class.mro()}')
s1 = S1class()
s1.text()

print(f'test3: S1class MRO: {S2class.mro()}')
s2 = S2class
s2.text()