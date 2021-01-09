#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from dbconfig import read_db_config

# db = pymysql.connect("192.168.56.33","geektimedev","geektimedev01!","testdb")
# db = pymysql.connect("192.168.56.33","geektimedev","geektimedev01!","testdb")
# 常用的存放配置的文件格式： ini yaml json

dbserver = read_db_config()
print(dbserver)
db = pymysql.connect(**dbserver)

try:
    with db.cursor() as cursor:
        sql = """ select version()"""
        # 使用execute（）方法执行 salq
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally:
    # 关闭数据库
    db.close()

print(f"Database version ：{result}")
