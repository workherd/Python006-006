#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/10 12:08
# @Author     : john
# @File       : c09_pic.py
import pandas as pd
import numpy as np

dates = pd.date_range('20200101', periods=12)
print(dates)
df = pd.DataFrame(np.random.randn(12,4), index=dates, columns=list('ABCD'))
print('*'*88)
print(df)

import matplotlib.pyplot as plt  # 需使用pip进行安装
plt.plot(df.index, df['A'],)
plt.show()
print('*'*88)
plt.plot(df.index, df['A'],)
plt.show()
print('*'*88)
plt.plot(df.index, df['A'],
         color='#FFAA00',  # 颜色
         linestyle='--',  # 线条样式
         linewidth=3,  # 线条宽度
         marker='D',  # 点标记
         )
plt.show()
print('*'*88)
# pip install seaborn
import seaborn as sns
print('*'*88)
# 绘制点散图
plt.scatter(df.index, df['A'])
plt.show()

# 美化plt
sns.set_style('darkgrid')
plt.scatter(df.index, df['A'])
plt.show()