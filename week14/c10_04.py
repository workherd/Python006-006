#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 14:52
# @Author     : john
# @File       : c10_04.py
import jieba
string = '极客大学Python进阶训练营真好玩'
user_dict  = r'extra_dict/user_dict.txt'

# 自定义字典
jieba.load_userdict(user_dict)

result = jieba.cut(string, cut_all=False)
print('自定义：'+'/'.join(list(result)))
print('='*88)

# 动态添加词典
jieba.add_word('极客大学')

#动态删除词典
jieba.del_word('自定义词')

result = jieba.cut(string, cut_all=False)
print('动态添加：'+'/'.join(list(result)))
print('='*88)

string2 = '我们中出了一个叛徒'
result = jieba.cut(string2, cut_all=False)

print('错误分词：'+'/'.join(list(result)))
print('='*88)

# 关闭自动计算词频
result=jieba.cut(string2, HMM=False)
print('关闭词频：'+'/'.join(result))
print('='*88)

# 调整分词，合并

jieba.suggest_freq('中出', True)

result=jieba.cut(string2,HMM=False)
print('分词合并：'+'/'.join(result))
print('='*88)

# 调整词频，分开分词
string3 = '如果放到Post中将出错'
jieba.suggest_freq(('中','将'), True)
result = jieba.cut(string3, HMM=False)
print('分开分词'+'/'.join(list(result)))

print('='*88)


print('='*88)
