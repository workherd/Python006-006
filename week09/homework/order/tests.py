from django.test import TestCase

# Create your tests here.

pass

"""
作业一：
使用 REST API 实现一个 Order（订单）类，并使用 json 展示数据，要求如下：

/orders 列出所有 order
/orders/{id} 列出具体的一个订单
/orders/create 只接受 Post 请求创建一个订单
/orders/{id}/cancel 接受 Get 请求，取消一个订单。 （提示： sql update）
选做：

/orders 列出所有 order 带分页功能
作业二：
基于 Django REST framework 实现用户接入控制功能

说明：

对作业一的 /orders/create 接口实现用户接入控制功能。
可以使用 SessionAuthentication 或 TokenAuthentication 实现。
选做：

使用 Json-Web-Token（JWT）认证方式实现

"""