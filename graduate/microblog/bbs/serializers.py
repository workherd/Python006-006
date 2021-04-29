#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/27 9:37
# @Author     : john
# @File       : serializers.py

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers
from .models import Articles,  Posts, UserScore
# from .models import UserProfile
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    author_id = serializers.ReadOnlyField(source='author_id.username')

    class Meta:
        model = Articles
        fields = ['id', 'author_id', 'body', 'createtime', 'title']

#
# class ProfileSerializer(serializers.HyperlinkedModelSerializer):
#     # other = OtherSerializer(read_only=True, many=True)
#     # class Meta:
#     #   fields = (..., 'other',)
#
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'nickname', 'phone_number', 'description', 'createtime', 'score']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'articles']


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        # exclude = ('password',)
        fields = ['url', 'id', 'username', 'email', 'password']

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs


class PostsSerializer(serializers.ModelSerializer):
    """ 评论序列 """

    class Meta:
        model = Posts
        fields = ['id', 'content', 'create_time', 'article_id', 'user_id']

    @api_view(['GET'])
    def showdata(request):
        id = request.GET['id']
        datas = Posts.objects.filter(article_id=id)
        postdata = PostsSerializer(datas, many=True)
        return Response({'data': PostsSerializer.data})
