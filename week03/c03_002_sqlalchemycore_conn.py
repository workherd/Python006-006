#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey

engine = create_engine("mysql+pymysql://geektimedev:geektimedev01!@192.168.56.33:3306/testdb", echo=True)
# echo = True 用户拍错，生产环境通常设置false
# 创建元数据
metadata = MetaData(engine)

book_table = Table('book',metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name',String(20)),
                   )
author_table = Table('author',metadata,
                     Column('id', Integer, primary_key=True),
                     Column('book_id', None, ForeignKey('book.id')),
                     Column('author_name', String(128), nullable=False),
                     )

try:
    metadata.create_all()
except Exception as e:
    print(f"creat error {e}")


