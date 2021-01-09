#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from dbutils.pooled_db import PooledDB

db_config = {
    "host": "192.168.56.33",
    "port": "3306",
    "user": "geektimedev",
    "passwd": "geektimedev01!",
    "db": "testdb",
    "charset": "utf8",
    "maxconnections": 0,
    "mincached": 4,
    "maxcached": 0,
    "maxusage": 5,
    "blocking": True,
}

spool = PooledDB(pymysql, **db_config)

conn = spool.connection()
cur = conn.cursor()
sql = "select * from bookorm;"
cur.execute(sql)
f = cur.fechall()
print(f)
cur.close()
conn.close()
