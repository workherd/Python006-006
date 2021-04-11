#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 7:39
# @Author     : john
# @File       : c03.py

import pandas as pd
#  pip install xlrd
# 导入excel
excel1 = pd.read_excel(r'1.xlsx')
print(excel1)

# 指定不同的表格
excel2 = pd.read_excel(r'1.xlsx', sheet_name=0)
print('*'*88)
print(excel2)

# 读取 csv
data_csv = pd.read_csv(r'd:\1.csv', sep=',', nrows=10, encoding='utf-8')
print('*'*88)
print(data_csv)

# 读取txt
data_txt = pd.read_table(r'file.txt', sep=' ')
print('*'*88)
print(data_txt)

import pymysql
sql = 'SELECT * from im_user limit 22'
conn = pymysql.connect('192.168.56.33', 'pydev', 'password@1234', 'iam', charset='utf8')
df = pd.read_sql(sql, conn)
print('*'*88)
print(df)

# 熟悉数据
# 显示前几行
print('*'*88)
print(excel1.head(22))

# 显示行列数量
print('*'*88)
print(excel1.shape)

# 详细信息
print('*'*88)
print(excel1.info())

print('*'*88)
print(excel1.describe())
print('*'*88)
print('*'*88)


