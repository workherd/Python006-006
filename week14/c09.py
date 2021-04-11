#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 12:03
# @Author     : john
# @File       : c09.py
import pandas as pd
import numpy as np
group = ['x', 'y', 'z']
df = pd.DataFrame({
    "group": [group[x] for x in np.random.randint(0, len(group), 10)],
    "age": np.random.randint(15, 50, 10)

})
#导出为xlsx文件，注意要安装xlwt插件
# 导出为.xlsx文件
df.to_excel( excel_writer=r'file.xlsx')

# 设置Sheet名称
df.to_excel( excel_writer=r'file.xlsx', sheet_name='sheet1')

# 设置索引,设置参数index=False就可以在导出时把这种索引去掉
df.to_excel( excel_writer=r'file.xlsx', sheet_name='sheet1', index = False)

# 设置要导出的列
df.to_excel( excel_writer=r'file.xlsx', sheet_name='sheet1',
             index=False, columns=['col1','col2'])

# 设置编码格式
enconding = 'utf-8'
enconding = 'gbk'  #  win下使用

# 缺失值处理
na_rep = 0 # 缺失值填充为0

# 无穷值处理
inf_rep = 0

# 导出为.csv文件
df.to_csv()

# 输出性能
df.to_pickle('xx.pkl')   #

agg(sum) # 快
agg(lambda x: x.sum()) # 慢
