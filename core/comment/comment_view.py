# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 11:38
# @Author  : NoWords
# @FileName: comment_view.py
from core.common.common_view import CommonAPIView
from ..serializers import CommentSerializer
from ..models import Comment


class CommentAPIView(CommonAPIView):
    """
   评论管理
   """

    model = Comment
    serializer = CommentSerializer
    add_insert_creator = True
    update_insert_updater = False
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'content__contains', 'request_key': 'content'},
    ]

