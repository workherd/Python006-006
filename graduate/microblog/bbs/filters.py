#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2021/2/28 1:20
# @Author     : john
# @File       : filters.py
from django_filters import rest_framework as rf_filters
from .models import Articles


class ArticlesFilters(rf_filters.FilterSet):
    # id = rs_filters.NumberFilter(field_name=‘id’， lookup_exp='lte')

    class Meta:
        model = Articles
        fields = ['title', 'body']