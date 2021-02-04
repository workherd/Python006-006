#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/1/30 21:06
# @Author     : john
# @File       : c11.py
# 使用type元类创建类

def pop_value(self, dict_value):
    for key in self.keys():
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break


# 元类要求，必须继承自type
class DelValue(type):
    # 元类要求，必须实现new方法
    def __new__(cls, name, bases, attrs):
        attrs['pop_value'] = pop_value
        return type.__new__(cls, name, bases, attrs)


class DelDictValue(dict, metaclass=DelValue):
    pass


d = DelDictValue()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d.pop_value('C')
for k,v in d.items():
    print(k,v)
