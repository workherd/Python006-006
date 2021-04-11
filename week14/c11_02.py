#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 22:51
# @Author     : john
# @File       : c11_02.py
import pandas as pd
from snownlp import SnowNLP

# 加载爬虫的原始评论数据
df = pd.read_csv('book_utf8.csv')
print(df)
print('='*88)
# 调整格式
df.columns = ['star', 'vote', 'shorts']
star_to_number = {
    '力荐': 5,
    '推荐': 4,
    '还行': 3,
    '较差': 2,
    '很差': 1,
}

df['new_star'] = df['star'].map(star_to_number)
print(df)
print('='*88)
print(df['new_star'])
print('='*88)
# 用第一个评论做测试
first_line = df[df['new_star'] == 3].iloc[0]
print(first_line)
print('='*88)
text = first_line['shorts']
print(text)
print('='*88)
s = SnowNLP(text)
print(f'情感倾向：{s.sentiments}, 文本内容：{text}')


# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments


df["sentiment"] = df.shorts.apply(_sentiment)
# 查看结果
print(df.head())
print('='*88)
# 分析平均值
print(df.sentiment.mean())
print('='*88)
del df['star']
del df['vote']
order = ['new_star', 'shorts', 'sentiment']
df = df[order]
print(df)
print('='*88)
df.rename(columns={'new_star':'n_star','shorts':'short'}, inplace=True)
df.to_csv('result.csv', index=None)
print('='*88)
