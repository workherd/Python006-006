#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 13:19
# @Author     : john
# @File       : c02_02.py
import pymysql

conn = pymysql.connect(
    host='192.168.56.33',
    port=3306,
    user='lixiaod',
    password='tasly',
    database='d03_test',
    charset='utf8'
)

# 获得cursor游标对象
con1 = conn.cursor()

# 操作行数
count = con1.execute('select * from tb1;')
print(f'查询到 {count} 条记录')

# 获取一条查询结果
result = con1.fetchone()
print(result)

# 获取所有查询结果

print(con1.fetchall())

con1.close()
conn.close()