#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika


# 生产者
# 用户名密码, 不同业务分配不同的账号密码
credential = pika.PlainCredentials('guest', 'guest')

# 虚拟队列需指定参数virtual_host,
parameters = pika.ConnectionParameters(host='192.168.56.33',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credential)

# 阻塞方法
connection = pika.BlockingConnection(parameters)

# 建立信道
channel = connection.channel()

# 建立队列，若不存在会自动创建， durable=True 时队列有持久化功能
channel.queue_declare(queue='direct_demo', durable=False)

# exchange指定交换机，routing_key指定队列名
channel.basic_publish(exchange='', routing_key='direct_demo',
                      body='send message to rabbitmq')

# 关闭与rabbitmq server的连接
connection.close()
