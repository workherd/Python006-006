#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 20:37
# @Author     : john
# @File       : c10_factory.py

class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Man(Human):
    def __init__(self, name):
        print(f'Hi, man {name}')


class Woman(Human):
    def __init__(self, name):
        print(f'Hi, woman {name}')


class Factory:
    def getPersion(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPersion('Adam', 'M')