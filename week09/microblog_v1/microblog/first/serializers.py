#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/14 23:09
# @Author     : john
# @File       : serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Articles


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Articles
        fields = ['url', 'id', 'articleid', 'article', 'createtime', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'articles']