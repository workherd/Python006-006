#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/13 7:18
# @Author     : john
# @File       : homework_teacher.py

class 动物(object):
    """
    不允许被实例化（abs）
    """

    def __init__(self, 类型, 体型, 性格):
        self.__类型 = 类型
        self.__体型 = 体型
        self.__性格 = 性格

    @property
    def 类型(self):
        return self.__类型

    @property
    def 体型(self):
        return self.__体型

    @property
    def 性格(self):
        return self.__类型

    @staticmethod
    def is_dangerous(self, 动物实例1):
        if self.体型 >= 中 and 食肉 and 凶猛:
            return True
        else:
            return False


class Cat(动物):
    叫声 = u"喵喵喵!"

    适合当宠物 = True

    def __init__(self, name, 类型, 体型, 性格):
        super().__init__(类型, 体型, 性格)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @classmethod
    def 叫声(cls):
        return cls.叫声


class Zoo(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_animal(self, 动物实例1):
        if not hasattr(self, 动物实例1.__class__.__name__):
            setattr(self, 动物实例1.__class__.__name__, [])
        getattr(self, 动物实例1.__class__.__name__).append(动物实例1)


if __name__ == '__main__':
    z = Zoo('时间动物园')

    cat1 = Cat('大花猫1', '食肉', '小', '温顺')

    z.add_animal(cat1)

    have_cat = getattr(z, 'Cat')


