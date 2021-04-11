#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/8 6:56
# @Author     : john
# @File       : c02_02.py
import pandas as pd

# 列表创建dataform
df1 = pd.DataFrame(['a', 'b', 'c', 'd'])
# 嵌套列表创建dataform
df2 = pd.DataFrame([
    ['a', 'b'],
    ['c', 'd']
])
print('df1\n', df1)
print('df2\n', df2)

# 自定义索引
df2.columns = ['one', 'two']
print('*'*88)
print('df2\n', df2)
df2.index = ['first', 'second']

print('*'*88)
print('df2\n', df2)

#  可以在创建时直接指定行索引和列索引，DataFram([...], columns='...', index='...')
# 查看索引
print(df2.columns, '11111',  df2.index)
print(type(df2.values))
