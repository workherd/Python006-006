#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 21:35
# @Author     : john
# @File       : c12.py
from abc import ABCMeta, abstractmethod


class Bases(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Bases):
    def foo(self):
        pass

    def bar(self):
        pass


c = Concrete() # TypeError
