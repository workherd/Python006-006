#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 8:51
# @Author     : john
# @File       : c04.py
import pandas as pd
import numpy as np

x = pd.Series([1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])

# 判断是否有缺失值
print(x.hasnans)

# 将缺失值填充为平均数
a = x.fillna(value=x.mean())
print('*'*88)
print(a)

# 前向填充缺失值
df3 = pd.DataFrame({
    "A": [5, 3, None, 4],
    "B": [None, 2, 4, 3],
    "C": [4, 3, 8, 5],
    "D": [5, 4, 2, None],
})
print('*'*88)
print(df3.isnull())
print(df3.isnull().sum())  # 查看缺失值汇总
print(df3.ffill())  # 用上一行填充
print(df3.ffill(axis=1))  # 用前一列填充

# 缺失值删除
print('*'*88)
print(df3.info())
print(df3.dropna())

# 填充缺失值
print('*'*88)
print(df3.fillna('无'))

# 填充缺失值
print('*'*88)
print(df3.drop_duplicates())   # 完全一致的去重

print('*'*88)