#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 11:22
# @Author     : john
# @File       : c08.py
import pandas as pd
import numpy as np

group = ['x', 'y', 'z']
data1 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10)

})
data2 = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "salary": np.random.randint(5, 50, 10),

})
data3=pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10),
    "salary": np.random.randint(5, 50, 10),

})
print(data1)
print(data2)
print(data3)
# 一对一
print('*'*88)
print(pd.merge(data1, data2))

#多对一
print('*'*88)
print(pd.merge(data3, data2, on='group'))
# 多堆多
print('*'*88)
print(pd.merge(data3, data2))

#连接键类型，解决没有公共列的问题
print('*'*88)
print(pd.merge(data3,data2,left_on='age', right_on='salary'))
#连接方式
# 内连接，组合连接方式，默认都是内连接
# 左连接 left ； 有连接 right ；外连接 outer

print('*'*88)
print(pd.merge(data3, data2, on='group', how='inner'))
# 纵向拼接
print('*'*88)
print(pd.concat([data1, data2]))
print('*'*88)
print('*'*88)
print('*'*88)
print('*'*88)