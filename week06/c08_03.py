#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 19:08
# @Author     : john
# @File       : c08_03.py

class BaseClass(object):
    num_base_calls = 0

    def call_me(self):
        print('Calling method on Bases Class')
        self.num_base_calls +=1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    # def call_me(self):
    #     print('Calling method on Left Subclass')
    #     self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_call = 0

    def call_me(self):
        print('Call method on Right Subclass')
        self.num_right_call += 1


class Subclass(LeftSubclass, RightSubclass):
    pass


a = Subclass()
a.call_me()
print(Subclass.mro())  # .mro()  可现实当前类的集成顺序

# 新式类中继承时 广度优先