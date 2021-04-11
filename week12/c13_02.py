#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/3/23 20:17
# @Author     : john
# @File       : c13_02.py

mylist = []
for i in range(1, 11):
    if i > 5:
        mylist.append(i**2)

print('mylist',mylist)

mylist2 = [i**2 for i in range(1, 11) if i>5]
print('mylist2',mylist2)

mydict = {'key1': 'value1', 'key2': 'value2'}
mylist2 = [key + ':' + value for key, value in mydict.items()]
print('mylist2-fromdict', mylist2)

mydict = {i: i*i for i in (5,6,7)}
print('dict ', mydict)
mydict2 = {value:key for key,value in mydict.items()}
print(mydict2)

mytuple = tuple(i for i in 'HarryPotter' if i not in 'er')  # 元组
print(mytuple, 'mytuple')
myset = {i for i in 'HarryPotter' if i not in 'er'}  #  集合
print(myset, 'myset')


mygenerator = (i for i in range(0, 11))
print(next(mygenerator))
print(next(mygenerator))
print(list(mygenerator))