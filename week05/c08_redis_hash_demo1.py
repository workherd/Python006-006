#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

client = redis.Redis(host='192.168.56.33', password='Tasly@@tasly1123')
# # 插入
# client.hset('vip_user', '1001', 1)
# client.hset('vip_user', '1002', 1)
# # 删除
# client.hdel('D', '1002')
# # 检查
# print(client.hexists('vip_user', '1001'))
# print(client.hexists('vip_user', '1002'))

# # 批量添加读个键值对
# d1 = {
#     '1003':1,
#     '1004':1,
# }
# client.hset('vip_user', *d1)

# 获取数据 hkeys hget hmget hgetall
filed = client.hkeys('vip_user')
print(filed)
print(client.hget('vip_user', '1001'))
print(client.hgetall('vip_user'))