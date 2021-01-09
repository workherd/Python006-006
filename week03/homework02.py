#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, Boolean, String, MetaData, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


class Person_table(Base):
    __tablename__ = 'person'
    id = Column(Integer(),primary_key=True)
    username = Column(String(15), nullable=False)
    age = Column(Integer())
    birthday = Column(DateTime())
    gender = Column(String(2))
    education = Column(String(4))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# 实例化一个引擎
dburl = "mysql+pymysql://geektimedev:geektimedev01!@192.168.56.33:3306/testdb?charset=utf8"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 创建表
try:
    Base.metadata.create_all(engine)  # 若存在则忽略
except Exception as e:
    print(e)

# 增加数据
# p1 = Person_table(username='a1', age=30, birthday='1999-03-02',gender='女',education='专科')
# p2 = Person_table(username='a2', age=30, birthday='1999-03-02',gender='女',education='专科')
# p3 = Person_table(username='a3', age=30, birthday='1994-05-02',gender='男',education='大学本科')
# session.add(p1)
# session.add(p2)
# session.add(p3)


result = session.query(Person_table).first()

#
# print(result)

session.commit()


print(result.username)
print(result.age)