#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/28 11:20
# @Author     : john
# @File       : urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order import views
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'orders', views.OrderAPIViewSet, 'order_list')
router.register(r'ordersapi', views.CreateOrderViewSet, 'order_api')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='ODS')),
]