#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 9:09
# @Author     : john
# @File       : c05.py
import pandas as pd
# 行列调整
df = pd.DataFrame({
    "A": [5, 3, None, 4],
    "B": [None, 2, 4, 3],
    "C": [4, 3, 8, 5],
    "D": [5, 4, 2, None],
})
print(df)

# 列的选择，多个列要用列表

print('*'*88)
print(df[['A', 'C']])

# 某些列
print('*'*88)
print(df.iloc[:, [0,2] ])  # :表示所有行，获得第一和第三列

# 行选择
print('*'*88)
print(df.loc[ [0, 2] ])  # 选择第1行和第3行
print(df.loc[ 0:2 ])  # 选择第1行到第3行

# 比较
print('*'*88)
print( df['A'] <5 )
print(df[( df['A']<5) & ( df['C']<4 )])

# 数值替换
# 一对一替换, 用于单个异常值处理
print('*'*88)
print(df['C'].replace(4, 40))

# 多对一替换
import numpy as np
print(df.replace(np.nan, 0))
print(df.replace([4, 5, 8], 1000))

# 多对多替换
print('*'*88)
print(df.replace({4: 400, 5: 500, 8: 800}))

# 排序
# 按照指定列降序排列
print('*'*88)
print(df.sort_values(by=['A'], ascending=False))
# 多列排序
print('*'*88)
print(df.sort_values(by=['A', 'C'], ascending=[True,False]))

# 删除
# 删除行
print('*'*88)
print(df.drop( 'A', axis=1))
# 删除行
print('*'*88)
print(df.drop(3, axis=0))
# 删除特定行
print('*'*88)
print(df[df['A'] < 4])


# 行列互换
print('*'*88)

print(df.T)
print(df.T.T)
# 索引重塑
print('*'*88)
df4 = pd.DataFrame([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ],
    columns=['one', 'two', 'three'],
    index= ['first', 'second'],
)
print(df4)
print('*'*88)
print(df4.stack())
print('*'*88)
print(df4.unstack())
print('*'*88)
print(df4.stack())
print(df4.stack().reset_index())
print('*'*88)
