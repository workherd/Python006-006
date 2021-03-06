#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/31 8:56
# @Author     : john
# @File       : c12_04.py
# Mixin类无法单独使用，必须和其他类混合使用，来加强其他类

str = 'starter'


class Displayer():
    def display(self, message):
        print(message)


class LoggerMinxin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super(LoggerMinxin, self).display(message)
        self.log(message)


class MySubClass(LoggerMinxin, Displayer):
    def log(self, message):
        super().log(message, filename='subclasslog.txt')


if __name__ == '__main__':
    subclass = MySubClass()
    subclass.display('This string will be shown and logged in subclasslog.txt')
    print(MySubClass.mro())
    print('end')
