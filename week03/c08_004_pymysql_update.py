#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

db = pymysql.connect("192.168.56.33","geektimedev","geektimedev01!","testdb")

try:
    with db.cursor() as cursor:
        sql = """ update book set name = %s where id = %s """
        value = ("水浒",1002)
        # 使用execute（）方法执行 sql
        cursor.execute(sql,value)
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally:
    # 关闭数据库
    db.close()
    print(cursor.rowcount)
