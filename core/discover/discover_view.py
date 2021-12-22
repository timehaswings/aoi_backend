# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/28 8:56
# @Author  : NoWords
# @FileName: discover_view.py
from core.common.common_view import CommonAPIView
from ..serializers import DiscoverSerializer
from ..models import Discover


class DiscoverAPIView(CommonAPIView):
    """
    发现管理
    """

    model = Discover
    serializer = DiscoverSerializer
    add_insert_creator = True
    update_insert_updater = True
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'is_active', 'request_key': 'isActive'},
        {'filter_key': 'name__contains', 'request_key': 'name'},
        {'filter_key': 'content__contains', 'request_key': 'content'},
    ]
