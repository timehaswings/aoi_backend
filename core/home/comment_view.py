# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/2/28 20:08
# @Author  : NoWords
# @FileName: comment_view.py

from core.serializers import CommentSerializer
from ..models import BaseVideo
from ..common.unlimited_data_view import UnlimitedDataView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CommentApiView(UnlimitedDataView):

    def get(self, request, *args, **kwargs):
        params = request.GET
        vid = params.get('id')
        if not vid:
            return Response({'msg': '参数错误', 'success': False}, status.HTTP_200_OK)
        page_size = params.get('pageSize')
        page_no = params.get('pageNo')
        video = BaseVideo.objects.filter(id=vid, is_delete=0, is_active=1).first()
        if not video:
            return Response({'msg': '视频未找到', 'success': False}, status.HTTP_200_OK)
        comment_list = video.comment_set.all()
        print(comment_list)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'total': 0,
                'rows': []
            }
        }
        return Response(result, status.HTTP_200_OK)
