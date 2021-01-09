#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

# db = pymysql.connect("192.168.56.33","geektimedev","geektimedev01!","testdb")
db = pymysql.connect("192.168.56.33","geektimedev","geektimedev01!","testdb")
# 常用的存放配置的文件格式： ini yaml json


try:
    with db.cursor() as cursor:
        sql = """ insert into book(id, name) values (%s,%s)"""
        value = (
            (1004,'三国演义'),
            (1005,'飘')
        )
        # 使用execute（）方法执行 salq
        cursor.executemany(sql,value)
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally:
    # 关闭数据库
    db.close()
    print(cursor.rowcount)
