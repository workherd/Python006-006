#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

client = redis.Redis(host='192.168.56.33', password='Tasly@@tasly1123')

print(client.keys())

for key in client.keys():
    print(key.decode())

print(client.keys('password'))
