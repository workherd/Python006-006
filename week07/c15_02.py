#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/13 20:05
# @Author     : john
# @File       : c15_02.py

# 迭代器有效性测试
a_dict = {'a':1, 'b':2}
a_dict_iter = iter(a_dict)  # 转换为迭代器
next(a_dict_iter)
a_dict['c'] = 3
next(a_dict_iter)   # 报错了，结论：字典插入内容后，迭代器就失效了，列表的尾部插入不会
