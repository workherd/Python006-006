#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 14:23
# @Author     : john
# @File       : c10.py
import jieba
strings = ['我来自极客大学‘，’Python进阶训练营真好玩']

for string in strings:
    result = jieba.cut(string, cut_all=False)  # 精确模式
    print('Default mode:'+'/'.join(list(result)))

for string in strings:
    result = jieba.cut(string, cut_all=True)  # 全模式
    print('Full Mode:'+'/'.join(list(result)))

result = jieba.cut('钟南山院士接受采访新冠不会二次爆发')  # 默认精确模式
print(list(result))
result = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print('Search Mode: '+'/'.join(list(result)))