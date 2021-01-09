#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(book_id=‘{self.book_id}’," \
            "book_name={self.book_name})".format(self=self)

class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(),default=datetime.now, onupdate=datetime.now)


# 业务逻辑
# 持久层    orm存在的价值
# 数据库层

# 实例化一个引擎
dburl = "mysql+pymysql://geektimedev:geektimedev01!@192.168.56.33:3306/testdb"
engine = create_engine(dburl, echo=True, encoding="utf-8")


# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()


# 更新
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 1)
query.update({Book_table.book_name: 'newbook'})
new_book = query.first()
print(new_book.book_name)

session.commit()

