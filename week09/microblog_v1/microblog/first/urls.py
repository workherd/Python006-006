#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/14 22:26
# @Author     : john
# @File       : urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from first import views
from django.conf.urls import include
from  rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'articles', views.ArticleAPIViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

]
