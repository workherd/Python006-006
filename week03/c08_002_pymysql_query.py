#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

db = pymysql.connect("192.168.56.33","geektimedev","geektimedev01!","testdb")

try:
    with db.cursor() as cursor:
        sql = """ SELECT name from book """
        # 使用execute（）方法执行 sql
        cursor.execute(sql)
        books = cursor.fetchall() # fetchone()
        for book in books:
            print(book)
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally:
    # 关闭数据库
    db.close()
    print(cursor.rowcount)
