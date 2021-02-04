#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 14:47
# @Author     : john
# @File       : c01.py


class Human(object):
    # 静态字段
    live = True

    def __init__(self, name):
        # 普通字段
        self.name = name  # self 表示示例化本身， 可以改成任意字符，但建议保持
        print("object init", self.name)

man = Human('Adam')
woman = Human('Eve')

# 查看类属性
a = Human.__dict__
print(a)
print(man.name)
man.live = False
a = man.__dict__
print('man dict',a)
print('woman dict', woman.__dict__ )

# 使用静态字段
print(Human.live)

# 为类添加静态字段
Human.netwattr = 1
print('dir', dir(Human))  # 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print('human_class', Human.__dict__)

# 默认类型不能添加属性
# setattr(list, 'newattr', 'value')   #  list.newattr = value

# 现实object类的所有子类
print('*'*88)
print('object cleasses', ().__class__.__bases__[0].__subclasses__() )  # 元组-》类型-》父类->现实其所有子类
print('*'*88)
print('man cleasses', man.__class__.__bases__[0].__subclasses__() )