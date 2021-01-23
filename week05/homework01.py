#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2021/1/23 18:57
# @Author: john
# @File: homework01.py


"""
作业一：使用 Python+redis 实现高并发的计数器功能
需求描述:
在社交类网站中，经常需要对文章、视频等元素进行计数统计功能，热点文章和视频多为高并发请求，因此采用 redis 做为文章阅读、视频播放的计数器。
请实现以下函数：

复制代码
counter()
def counter(video_id: int):
    ...
    return count_number
函数说明:

counter 函数为统计视频播放次数的函数，每调用一次，播放次数 +1
参数 video_id 每个视频的 id，全局唯一
基于 redis 实现自增操作，确保线程安全
期望执行结果：
conuter(1001) # 返回 1
conuter(1001) # 返回 2
conuter(1002) # 返回 1
conuter(1001) # 返回 3
conuter(1002) # 返回 2
"""

import redis
client = redis.Redis(host='192.168.56.33', password='Tasly@@tasly1123')


def counter(video_id: int):
    if client.get(video_id):
        client.incr(video_id)
    else:
        client.set(video_id, 1, nt=True)
    count_number =client.get(video_id)
    print(count_number.decode())
    return count_number


if __name__ == '__main__':
    counter(10002)