#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/14 23:14
# @Author     : john
# @File       : permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """ 自定义权限，只允许对象的所有者编辑"""

    def has_object_permission(self, request, view, obj):
        # 读取权限任何请求，我们总是允许GET HEAD或OPTTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该微博的所有者才允许写权限
        return obj.owner == request.user