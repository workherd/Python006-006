#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/18 20:50
# @Author     : john
# @File       : homework_demo.py
from abc import ABCMeta


class Zoo:

    def __init__(self, name) -> None:
        self.name = name
        self.zoo = set()

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError(f'expected an Animal instance')
        self.zoo.add(animal)

    def remove_animal(self, animal):
        if animal not in self.zoo:
            raise AttributeError(f'no attribute {animal}')
        self.zoo.remove(animal)

    def __repr__(self) -> str:
        return f'Zoo({self.name!r})'

    def __contains__(self, animal):
        return animal in self.zoo

    @property
    def size(self):
        return len(self.zoo)

    def __getattr__(self, item):
        try:
            count = sum(isinstance(i, eval(item)) for i in self.zoo)
            if count:
                self.__dict__[item] = count
        except NameError as e:
            print(e)


class Animal(metaclass=ABCMeta):
    varities = ('素食', '杂食', '食肉')
    figures = ('小', '中', '大', '特别大')
    characters = ('温顺', '中性', '凶猛')

    def __init__(self, varity, figure, character) -> None:
        self.varity = varity
        self.figure = figure
        self.character = character

    @property
    def varity(self):
        return self._varity

    @varity.setter
    def varity(self, value):
        if value not in self.varities:
            raise ValueError('可选项：素食、杂食、食肉')
        self._varity = value

    @property
    def figure(self):
        return self._figure

    @figure.setter
    def figure(self, value):
        if value not in self.figures:
            raise ValueError('可选项：小、中、大、特别大')
        self._figure = value

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, value):
        if value not in self.characters:
            raise ValueError('可选项：温顺、中性、凶猛')
        self._character = value

    def is_fierce(self):
        return self.varity == '食肉' and self.figures.index(self.figure) >= 1 and self.character == '凶猛'


class Cat(Animal):
    sound = 'miao'
    __slots__ = ['name']

    def __init__(self, name, varity, figure, character) -> None:
        self.name = name
        super().__init__(varity, figure, character)

    def petable(self):
        return self.is_fierce() is False

    @classmethod
    def meow(cls):
        return cls.sound

    def __repr__(self) -> str:
        return f'Cat({self.name!r})'


class Dog(Animal):
    sound = 'wang'
    __slots__ = ['name']

    def __init__(self, name, varity, figure, character) -> None:
        self.name = name
        super().__init__(varity, figure, character)

    def petable(self):
        return self.is_fierce() is False

    @classmethod
    def bark(cls):
        return cls.sound

    def __repr__(self) -> str:
        return f'Dog({self.name!r})'


class AnimalFactory:
    def product_animal(self, name, varity, figure, character, type_):
        if type_ == 'C':
            return Cat(name, varity, figure, character)
        elif type_ == 'D':
            return Dog(name, varity, figure, character)
        else:
            pass


if __name__ == '__main__':
    shanghaizoo = Zoo('上海浦东动物园')
    print(shanghaizoo, shanghaizoo.size)
    cat1 = Cat('大花猫', '食肉', '小', '温顺')
    print(cat1.name, cat1.sound, cat1.meow(), cat1.is_fierce(), cat1.petable())
    animalfactory = AnimalFactory()
    cat2 = animalfactory.product_animal('大橘', '杂食', '中', '中性', 'C')
    shanghaizoo.add_animal(cat1)
    shanghaizoo.add_animal(cat1)
    shanghaizoo.add_animal(cat2)
    print(cat2.name, cat2.sound, cat2.meow(), cat2.is_fierce(), cat2.petable())
    print(shanghaizoo.size, hasattr(shanghaizoo, 'Cat'), shanghaizoo.Cat)
    shanghaizoo.remove_animal(cat2)
    dog1 = animalfactory.product_animal('擎天柱', '食肉', '大', '凶猛', 'D')
    print(dog1.name, dog1.sound, dog1.bark(), dog1.is_fierce(), dog1.petable())
    # shanghaizoo.remove_animal(dog1)
    # shanghaizoo.add_animal(111)