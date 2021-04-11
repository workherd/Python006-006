#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/6 21:29
# @Author     : john
# @File       : c01_02_pandasFirst.py
import pandas as pd
import numpy as np  # 用来做数学分析
import matplotlib as plt  # 视觉显示

import os
pwd = os.path.dirname(os.path.realpath(__file__))
book = os.path.join(pwd, 'book_utf8.csv')
df = pd.read_csv(book)

# 输出全部内容
# print(df)

# 筛选包含还行的内容
print(df['还行'])
print('*'*88)

# 切片，显示前三行
print(df[0:2])
print('*'*88)

# 增加列名
df.columns = ['star', 'vote', 'shorts']
print(df)
print('*'*88)

# 过滤数据
print(df['star'] == '力荐')
print('*'*88)
print(df[df['star'] == '力荐'])
print('*'*88)

# 缺失数据
df.dropna()  # 通常做法-删除
print('*'*88)

# 数据聚合
a = df.groupby('star').sum()
print(a)
print('*'*88)

# 创建新列
star_to_number = {
    '力荐': 5,
    '推荐': 4,
    '还行': 3,
    '较差': 2,
    '很差': 1,
}
df['new_star'] = df['star'].map(star_to_number)
print(df)
