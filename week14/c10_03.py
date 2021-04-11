#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 14:36
# @Author     : john
# @File       : c10_02.py
import jieba
import jieba.analyse
text = '机器学习，需要一定的数据基础，需要掌握的数据基础知识特别多，如果从头到尾开始学，估计大部分人来不及学习深造'
stop_words = r'extra_dict/stop_words.txt'

jieba.analyse.set_stop_words(stop_words)

textrank = jieba.analyse.textrank(text,
                                  topK=5,
                                  withWeight=False)

print(list(textrank))

import pprint
pprint.pprint(textrank)