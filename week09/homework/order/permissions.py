#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/28 13:01
# @Author     : john
# @File       : permissions.py

from rest_framework import permissions


class IsManagerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or obj.manager:
            return True
        else:
            return False
