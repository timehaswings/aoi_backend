# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 9:02
# @Author  : NoWords
# @FileName: group_view.py
from core.common.common_view import CommonAPIView
from django.contrib.auth.models import Group

from core.serializers import GroupSerializer


class GroupAPIView(CommonAPIView):
    model = Group
    serializer = GroupSerializer
    filters = None
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
    ]

