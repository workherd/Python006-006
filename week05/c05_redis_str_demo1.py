#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

client = redis.Redis(host='192.168.56.33', password='Tasly@@tasly1123')

client.set('key','value')
client.set('key2','value2', nx=True)
result = client.get('key')
print(result)
client.append('key', 'value4')
result = client.get('key')
print(result)
print(result.decode())
print(client.get('key12'))
client.set('key12', 11, nx=True)
# client.incr('key12')  # +1
client.decr('key12')  # -1
print(client.get('key12'))
