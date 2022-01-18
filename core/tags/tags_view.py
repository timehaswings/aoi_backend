# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/25 10:04
# @Author  : NoWords
# @FileName: tags_view.py
from core.common.common_view import CommonAPIView
from ..serializers import TagsSerializer
from ..models import Tags


class TagsAPIView(CommonAPIView):
    """
    标签管理
    """

    model = Tags
    serializer = TagsSerializer
    add_insert_creator = True
    update_insert_updater = True
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'is_active', 'request_key': 'isActive', 'type': 'boolean'},
        {'filter_key': 'name__contains', 'request_key': 'name'},
    ]
