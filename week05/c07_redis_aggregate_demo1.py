#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis

client = redis.Redis(host='192.168.56.33', password='Tasly@@tasly1123')

print(client.sadd('redis_set_demo', 'new_data'))
# client.spop()
# 查看值
data = client.smembers('redis_set_demo')
print(data)

# 集合的运算
# 交集
client.sinter('set_a', 'set_b')

# 并集
client.sunion('set_a', 'set_b')

# 差集
client.sdiff('set_a', 'set_b')

