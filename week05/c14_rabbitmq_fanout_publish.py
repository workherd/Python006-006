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
channel.exchange_declare(exchange='logs',
                      exchange_type='fanout')  # 默认是derict

# exchange指定交换机，routing_key指定队列名
message = 'send message to task_queue'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message,
                      )

# 关闭与rabbitmq server的连接
connection.close()
