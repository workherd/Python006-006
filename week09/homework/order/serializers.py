#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/28 11:21
# @Author     : john
# @File       : serializers.py

from rest_framework import serializers
from .models import Orders


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    order_stream_id = serializers.ReadOnlyField(source='order_stream_id.username')

    class Meta:
        model = Orders
        fields = ['url', 'order_stream_id', 'body', 'is_effective', 'createtime']


class CreateOrderSerializer(serializers.HyperlinkedModelSerializer):

    # manager = serializers.PrimaryKeyRelatedField(many=, queryset=Orders.objects.all())

    class Meta:
        model = Orders
        fields = ['url', 'order_stream_id', 'body']