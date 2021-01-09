#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, Boolean, DECIMAL, String, MetaData, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime
import sys
import os

Base = declarative_base()

class Users_table(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, comment='用户名')

class Finance_table(Base):
    __tablename__ = 'finance'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'), comment='用户ID')
    money = Column(DECIMAL(precision=9, scale=2), nullable=False, comment='账户金额')
    created_on = Column(DateTime(), default=datetime.now, comment='创建时间')
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now, comment='更新时间')

class Finance_transfer_detail_table(Base):
    __tablename__ = 'finance_transfer_detail'
    id = Column(Integer(), primary_key=True)
    user_from = Column(Integer, ForeignKey(Users_table.id), comment='付款人')
    user_to = Column(Integer, ForeignKey(Users_table.id), comment='收款人')
    money = Column(DECIMAL(precision=9, scale=2), nullable=False, comment='转账金额')
    created_on = Column(DateTime(), default=datetime.now)

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
# u1 = Users_table(username='张三')
# u2 = Users_table(username='李四')
# session.add(u1)
# session.add(u2)
#
# f1 = Finance_table(user_id='1', money='130')
# f2 = Finance_table(user_id='2', money='33')
# session.add(f1)
# session.add(f2)

# 执行原生sql语句
# sql = 'select * from users'
# objs = session.execute(sql)
# session.commit()

# 转账
source_user = '张三'
destination_user = '李四'
trans_money = 100

connection = engine.connect(close_with_result=True)
trans = connection.begin()
try:
    # print('start1111')
    # source user 扣除金额
    step1 = session.query(Users_table).filter(Users_table.username == source_user).first()
    s_money = session.query(Finance_table).filter(Finance_table.user_id == step1.id).first()
    if s_money.money < 0:
        # raise UserWarning(f'{source_user}余额不足，转账失败')
        print(f'{source_user}余额不足，转账失败')
        trans.rollback()
    session.query(Finance_table).filter(Finance_table.user_id == step1.id).update(
        {Finance_table.money: s_money.money - trans_money})

    # destination_user 增加金额
    step2 = session.query(Users_table).filter(Users_table.username == destination_user).first()
    d_money = session.query(Finance_table).filter(Finance_table.user_id == step2.id).first()
    session.query(Finance_table).filter(Finance_table.user_id == step2.id).update(
        {Finance_table.money: d_money.money + trans_money})

    # 添加日志
    trans_log = Finance_transfer_detail_table(user_from=step1.id,user_to=step2.id,money=trans_money)
    session.add(trans_log)
    session.commit()
except Exception as e:
    print(e)
    trans.rollback()
    raise
finally:
    print('trans module ok end')
    connection.close()
print('this is the end')

#
# print(type(objs))
# print(objs)
# for i in objs:
#     print(i)

"""

connection = engine.connect(close_with_result=True)
trans = connection.begin()
try:
    r1 = connection.execute("update account set blance-=100 where id=1")
    r1 = connection.execute("update account set blance+=100 where id=2")
    trans.commit()
except:
    trans.rollback()
    raise
   

with engine.begin() as connection:
    r1 = connection.execute("update account set blance-=100 where id=1")
    r1 = connection.execute("update account set blance+=100 where id=2")
    

user1 = session1.query(User).with_lockmode('read').get(1)  
user2 = session1.query(User).with_lockmode('read').get(2)  
if user1.money >= 100:  
    user1.money -= 100  
    user2.money += 100  
    session1.add(TanseferLog(from_user=1, to_user=2, amount=100))  
user1 = session2.query(User).with_lockmode('read').get(1)  
user2 = session2.query(User).with_lockmode('read').get(2)  
if user1.money >= 100:  
    user1.money -= 100  
    user2.money += 100  
    session2.add(TanseferLog(from_user=1, to_user=2, amount=100))  
session1.commit()  
session2.commit()  
现在在执行 session1.commit() 的时候，因为 user1 和 user2 都被 session2 加了读锁，所以会等待锁被释放。超时以后，session1.commit() 会抛出个超时的异常，如果捕捉了的话，或者 session2 在另一个进程，那么 session2.commit() 还是能正常提交的。这种情况下，有一个事务是肯定会提交失败的，所以那些更改等于白做了。

接下来看看写锁，把上段代码中的 'read' 改成 'update' 即可。这次在执行 select 的时候就会被阻塞了：
user1 = session2.query(User).with_lockmode('update').get(1)
这样只要在超时期间内，session1 完成了提交或回滚，那么 session2 就能正常判断 user1.money >= 100 是否成立了。
由此可见，如果需要更改数据，最好加写锁。

那么什么时候用读锁呢？如果要保证事务运行期间内，被读取的数据不被修改，自己也不去修改，加读锁即可。
举例来说，假设我查询一个用户的开支记录（同时包含余额和转账记录），可以直接把 user 和 tansefer_log 做个内连接。
但如果用户的转账记录特别多，我在查询前想先验证用户的密码（假设在 user 表中），确认相符后才查询转账记录。而这两次查询的期间内，用户可能收到了一笔转账，导致他的 money 字段被修改了，但我在展示给用户时，用户的余额仍然没变，这就不正常了。
而如果我在读取 user 时加了读锁，用户是无法收到转账的（因为无法被另一个事务加写锁来修改 money 字段），这就保证了不会查出额外的 tansefer_log 记录。等我查询完两张表，释放了读锁后，转账就可以继续进行了，不过我显示的数据在当时的确是正确和一致的

"""