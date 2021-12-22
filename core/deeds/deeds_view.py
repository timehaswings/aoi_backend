# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 12:59
# @Author  : NoWords
# @FileName: deeds_view.py
from core.common.common_view import CommonAPIView
from ..serializers import DeedsSerializer
from ..models import Deeds


class DeedsAPIView(CommonAPIView):
    """
    活动管理
    """

    model = Deeds
    serializer = DeedsSerializer
    add_insert_creator = True
    update_insert_updater = True
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'title__contains', 'request_key': 'title'},
        {'filter_key': 'content__contains', 'request_key': 'content'},
    ]
