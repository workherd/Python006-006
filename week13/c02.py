#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/3 10:02
# @Author     : john
# @File       : c02.py
import pymysql

dbInfo = {
    'host': '192.168.56.33',
    'port': 3306,
    'user': 'lixiaod',
    'password': 'tasly',
    'db': 'd03_test'
}

sqls = ['select 1', 'select VERSION()']

result = []


class ConnDB(object):
    def __init__(self, dbinfo, sqls):
        self.host = dbinfo['host']
        self.port = dbinfo['port']
        self.user = dbinfo['user']
        self.password = dbinfo['password']
        self.db = dbinfo['db']
        self.sqls = sqls
        # self.run()

    def run(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except Exception as e:
            conn.rollback()
        # 关闭数据连接
        conn.close()


if __name__ == '__main__':
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(result)



