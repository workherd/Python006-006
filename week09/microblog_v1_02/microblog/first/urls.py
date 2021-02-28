#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/21 10:35
# @Author     : john
# @File       : urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from first import views
from django.conf.urls import include


router = DefaultRouter()
router.register(r'articles', views.ArticleAPIViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # 通过defaultrouter加载
]