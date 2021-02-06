#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/6 9:51
# @Author     : john
# @File       : c02.py

old_list = [i for i in range(1, 11)]
print(old_list)
new_list1 = old_list
print(new_list1)
new_list2 = list(old_list)  # 此时会开辟新的内存区域
print(new_list2)
print(new_list1 is new_list2)

# 切片
new_list3 = old_list[:]
print(new_list3)
print(new_list3 is old_list)  # 使用切片时也会产生新的内存区域

# 签到对象
old_list.append([11, 12])
print(old_list)
print(new_list1)
print(new_list2)
print(new_list3)


# 深入到对象内部复制，深拷贝
# 只拷贝内存地址，浅拷贝  # 深浅拷贝只对容器序列有效，容器只是传的是对象的引用
import copy
new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)

# assert new_list4 == new_list5   # 断言 True
# assert new_list4 is new_list5   # false

old_list[10][0] = 13
print(old_list)
print(new_list4)
print(new_list5)
