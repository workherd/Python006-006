#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika

# 消费者
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

# 定义一个回调函数来处理消息队列中的消息
def callback(ch, method, properties, body):
    # 手动发送消息 ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())

# 消费者使用队列和回调函数处理消息
channel.basic_consume('direct_demo', on_message_callback=callback)

# 开始接受消息，进入阻塞状态
channel.start_consuming()
