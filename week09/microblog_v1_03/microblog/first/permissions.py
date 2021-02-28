#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/21 12:24
# @Author     : john
# @File       : permissions.py
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
