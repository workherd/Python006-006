#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 14:36
# @Author     : john
# @File       : c10_02.py
import jieba.analyse
text = '机器学习，需要一定的数据基础，需要掌握的数据基础知识特别多，如果从头到尾开始学，估计大部分人来不及学习深造'
# 基于tf-idf算法进行关键词抽取
tfidf = jieba.analyse.extract_tags(text,
                                   topK=5,      # 权重醉倒的topk个关键词
                                   withWeight=True)  # 返回每个关键字的权重值
print(tfidf)
textrank = jieba.analyse.textrank(text,
                                  topK=5,
                                  withWeight=False)

print(textrank)

import pprint
pprint.pprint(tfidf)
pprint.pprint(textrank)