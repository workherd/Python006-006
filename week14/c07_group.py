#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 10:50
# @Author     : john
# @File       : c07_group.py
import pandas as pd
import numpy as np

# 聚合
sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
print(sales)
df2 = pd.DataFrame(sales)
print('*'*88)
print(df2)
print('*'*88)
print(df2.groupby('type').groups)
print('*'*88)
for a, b in df2.groupby('type'):
    print(a)
    print(b)
# 聚合后在计算
print('*'*88)
print(df2.groupby('type').count())

# 各类型产品的销售数量和销售总额
print('*'*88)
print(df2.groupby('type').aggregate({'type':'count', 'Feb':'sum'}))

print('*'*88)
group = ['x', 'y', 'z']
data = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10),
    "age": np.random.randint(15, 50, 10)

})
print(data)

print('*'*88)
print(data.groupby('group').agg('mean'))
print('*'*88)
print(data.groupby('group').mean())
print(data.groupby('group').mean().to_dict())
print('*'*88)
print(data.groupby('group').transform('mean'))

# 数据透视表
print('*'*88)
a = pd.pivot_table(data,
               values='salary',
               columns='group',
               index='age',
               aggfunc='count',
               margins=True
            ).reset_index()
print(a)
print('*'*88)