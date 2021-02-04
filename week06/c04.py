#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/26 18:36
# @Author     : john
# @File       : c04.py

import datetime


class Story(object):
    snake = 'python'

    def __init__(self, name):
        self.name = name

    # 静态方法
    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 3:
            print('god is coming')
        else:
            print('haha')


Story.god_come_go()