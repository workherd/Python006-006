#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 10:06
# @Author     : john
# @File       : c06.py
import pandas as pd
df = pd.DataFrame({"A": [5, 5, None, 4],
                   "B": [None, 2, 4, 3],
                   "C": [4, 3, 8, 5],
                   "D": [5, 4, 2, None]
                   })
print(df)

# 算数运算
# 两列之间的加减乘除
print('*'*88)
print(df['A'] + df['C'])

# 任意一列加减常数值，
print('*'*88)
print(df['A'] + 10)

# 比较运算
print('*'*88)
print(df['A'] < df['C'])

#count非空值
print('*'*88)
print(df.count())

#非空列求和
print('*'*88)
print(df.sum())
print('*'*88)
print(df['A'].sum())
print('*'*88)

# mean 求平均数，max最大值，min最小值，median中位数，mode众数，var方差，std标准差
print('*'*88)
