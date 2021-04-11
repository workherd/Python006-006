#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/4/6 21:00
# @Author     : john
# @File       : c01.py
from sklearn import datasets
# 鸢尾花数据集
iris = datasets.load_iris()
x, y = iris.data, iris.target

# for i in x:
#     print(i)
#
# for i in y:
#     print(i)

# 查看特征
print(iris.feature_names)

# 查看标签
print(iris.target_names)

# 按照3比1的比例划分训练集和测试集
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)


# load_xxx 各种数据集
# load_boston Boston房屋价格 回归
# load_digits 手写体  分类
# load_iris   鸢尾花 分类聚类