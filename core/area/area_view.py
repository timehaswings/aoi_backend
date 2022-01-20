# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/20 10:51
# @Author  : NoWords
# @FileName: area_view.py

from core.common.common_view import CommonAPIView
from ..serializers import AreaSerializer
from ..models import Area


class AreaAPIView(CommonAPIView):
    """
    分类管理
    """

    model = Area
    serializer = AreaSerializer
    filters = {}
    add_insert_creator = False
    update_insert_updater = False
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'name__contains', 'request_key': 'name'},
    ]