#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/24 14:06
# @Author     : john
# @File       : homework01.py


"""
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')

具体要求：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
"""


class Animal(object):
    def __init__(self, animal_type, shape, character):
        self.animal_type = animal_type   # 类型
        self.shape = shape  # 体型
        self.character = character  # 性格
        if self.animal_type == '食肉' and ( self.shape == '中' or self.shape == '大') and self.character == '性格凶猛':
            self.isferocious = True
        else:
            self.isferocious = False


class Cat(Animal):
    sound = 'miaomiaomiao'

    def __init__(self, name, animal_type, shape, character):
        super().__init__(animal_type, shape, character)
        if not self.isferocious:
            self.is_fit_Pets = True
        else:
            self.is_fit_Pets = False
        self.name = name


class Dog(Animal):
    sound = 'wangwangwang'

    def __init__(self, name, animal_type, shape, character):
        super().__init__(animal_type, shape, character)
        if not self.isferocious:
            self.is_fit_Pets = True
        else:
            self.is_fit_Pets = False
        self.name = name


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animal_list = []

    def add_animal(self, name):
        if name.name not in self.animal_list:
            self.animal_list.append(name.name)
            print(f'{name.name} 成功添加到 {self.name} 了')
        else:
            print(f'{name.name}已存在,添加失败')


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    print(cat1.name)
    print(cat1.isferocious)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    print('add again')
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    print()
    have_cat = hasattr(z, 'animal_list')
    have_cat = hasattr(z, 'Cat')
    print(have_cat)

