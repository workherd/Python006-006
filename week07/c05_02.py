#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 11:49
# @Author     : john
# @File       : c05_02.py

# L G
x = 'Global'
def func2():
    x = 'Enclosing'

    def func3():
        x = 'local'
        print('22',x)

    func3()

print('11',x)
func2()

# E
x = 'Global'


def func4():
    x = 'Enclosing'

    def func5():
        return x
    return func5


var = func4()
print(var())


# B
print(dir(__builtins__))