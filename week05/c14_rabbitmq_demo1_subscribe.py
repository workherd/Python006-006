#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika
import time

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
channel.queue_declare(queue='task_queue', durable=True)

# 定义一个回调函数来处理消息队列中的消息
def callback(ch, method, properties, body):
    time.sleep(1)
    # 手动发送消息 ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 如果该消费者的channel上未确认的消息数叨叨了prefetch_count数，则不向该消费者发送消息
channel.basic_qos(prefetch_count=1)

# 消费者使用队列和回调函数处理消息
channel.basic_consume('task_queue', callback)

# 开始接受消息，进入阻塞状态
channel.start_consuming()
