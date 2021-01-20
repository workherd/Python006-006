#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

client = redis.Redis(host='192.168.56.33', password='Tasly@@tasly1123')

# client.zadd('rank', {'a': 4, 'b': 3, 'c': 1, 'd': 2, 'e': 5})
# client.zincrby('rank', -2, 'e')
aa = client.zrangebyscore('rank', 1, 5)  # 从小到大
print(aa)
# zrevrank 从大到小
# 基card
aa = client.zcard('rank')
print(aa)

# 显示评分
print(client.zrange('rank', 0, -1, withscores=True))
print(client.zrange('rank', 0, 2, withscores=True))

print(client.zrevrange('rank', 0, 2, withscores=True))