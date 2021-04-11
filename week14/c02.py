#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/7 21:42
# @Author     : john
# @File       : c02.py
import pandas as pd
import numpy as np

# 从列表创建series
a = pd.Series(['a', 'b', 'c'])
print(a)

print('*'*88)

# 通过字典创建带索引的series
s1 = pd.Series({'a':11, 'b':22, 'c':33})
print(s1)
print('*'*88)
# 通过关键字穿件带索引的series
s2 = pd.Series([11, 22, 33], index=['a', 'b', 'c'])
print(s2)

# 获取全部索引
print('*'*88)
print(s1.index)
# 获取全部值
print('*'*88)
print(s1.values)
print('*'*88)

# 类型
print(type(s1.values))
print(type(np.array(['a', 'b', 'c'])))
print('*'*88)

# 转换为列表
print(s1.values.tolist())
print('*'*88)
# 使用index会提升查询性能。若index唯一，pandas会使用哈希表优化，查询性能为O（1）
#若index有序不唯一，pandas会使用二分查找算法，查询性能为O(logN)
# 若index完全碎金，每次查询会扫描全表，查询性能为O(N)

# 取出email
emails = pd.Series(['bcs at amazon.com', 'admin@163.com', 'mat@m.at', 'ab@abc.com'])
import re
pattern = '[A-Za-z0-9._]+@[A-Za-z0-9._]+\\.[A-Za-z]{2,5}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
print('mask\n',mask)
a = emails[mask]
print('emails\n',a)
