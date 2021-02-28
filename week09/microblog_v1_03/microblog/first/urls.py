#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/21 12:10
# @Author     : john
# @File       : urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from first import views
from django.conf.urls import include

router = DefaultRouter()
router.register(r'articles1', views.ArticleAPIViewSet)
router.register(r'users1', views.UserViewset)

urlpatterns = [
    path('', include(router.urls)),

]
