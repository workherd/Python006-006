#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 15:12
# @Author     : john
# @File       : c11.py
from snownlp import SnowNLP
text = '其实故事本来真的只值三星当初的中篇就足够了但是啊看到最后我又一次被东野叔的反战思想打动了所以就加多一星吧'
s = SnowNLP(text)

# 中文分词
print('='*88)
print(s.words)
# 词性标注（隐马尔可夫模型）
print(list(s.tags))
print('='*88)
#情感分析(朴素贝叶斯分类器)
print(s.sentiments)
text2 = '这本书烂透了'
s2 = SnowNLP(text2)
print(s2.sentiments)
print('='*88)
# 转拼音（trie数）
print(s.pinyin)

# 繁体转简体
text3 = '後面這些是繁體字'
s3 = SnowNLP(text3)
print(s3.han)
print('='*88)

# 提取关键字
print(s.keywords(limit=5))
print('='*88)
# 信息均衡
print(s.tf)  # 词频越大越重要
print(s.idf)  # 包括此条的文档越少，n越小 idf越大 说明此条越重要
print('='*88)
# 训练
# from snownlp import seg
# seg.train('data.txt')
# seg.save('seg.marshal')
# 修改snownlp/seg/__init__.py的data_path指向新的模型极客，通常由算法工程师提供


