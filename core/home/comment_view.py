# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/2/28 20:08
# @Author  : NoWords
# @FileName: comment_view.py

from core.serializers import CommentSerializer
from ..models import BaseVideo, Comment
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
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = CommentSerializer(comment_list[start:end], many=True).data
        else:
            rows = CommentSerializer(comment_list, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'total': comment_list.count(),
                'rows': rows
            }
        }
        return Response(result, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        video_id = data.get('video_id')
        if not video_id:
            return Response({'msg': '参数错误', 'success': False}, status.HTTP_200_OK)
        video = BaseVideo.objects.filter(id=video_id, is_delete=0, is_active=1).first()
        if not video:
            return Response({'msg': '视频未找到', 'success': False}, status.HTTP_200_OK)
        comment = Comment.objects.create(video=video, **data)
        result = {
            'msg': '添加数据成功',
            'success': True,
            'data': CommentSerializer(comment).data
        }
        return Response(result, status.HTTP_200_OK)
