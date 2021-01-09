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


# 增加数据
book_demo = Book_table(book_name='肖申克的救赎111')
book_demo2 = Book_table(book_name='活着')
book_demo3 = Book_table(book_name='聊斋')
# author_demo = Author_table()
# print(author_demo)
# print(book_demo)
session.add(book_demo)
# session.add(book_demo2)
# session.add(book_demo3)
# session.flush()
# session.commit()

# result = session.query(Book_table).all()
# result = session.query(Book_table).first()
# for result in session.query(Book_table):
#     print(result)
# first()  返回第一个
# one()  返回不是一个就报错
# scalar() 返回第一个第一个元素，多个结果就异常

# session.query(Book_table.book_name).first()

# 排序
# for result in session.query(Book_table.book_name).order_by(Book_table.book_id):
#     print(result)
# for result in session.query(Book_table.book_name, Book_table.book_id).order_by(desc(Book_table.book_id)):
#     print(result)
#
# query = session.query(Book_table).order_by(desc(Book_table.book_id)).limit(3)
# print([result.book_name for result in query])

# from sqlalchemy import func
# result = session.query(func.count(Book_table.book_name)).first()
# print(result)

# print( session.query(Book_table).filter(Book_table.book_id<8).first() )
#
# filter( Book_table.book_id > 10, Book_table.book_id<20 )

# from sqlalchemy import and_, or_, not_
# filter(
#     or_(
#         Book_table.xxx.between(100,100),
#         Book_table.yyy.contains('book')
#     )
# )



session.commit()