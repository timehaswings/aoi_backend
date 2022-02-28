# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/2/26 9:24
# @Author  : nowords
# @FileName: recommend_view.py
import random

from core.serializers import BaseVideoSerializer
from ..models import Tags, BaseVideo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class RecommendApiView(APIView):

    def get(self, request, *args, **kwargs):
        params = request.GET
        vid = params.get('id')
        if not vid:
            return Response({'msg': '参数错误', 'success': False}, status.HTTP_200_OK)
        limit = params.get('limit', 6)
        video = BaseVideo.objects.filter(id=vid, is_delete=0, is_active=1).first()
        if not video:
            return Response({'msg': '视频未找到', 'success': False}, status.HTTP_200_OK)
        tags_list = video.tags.all()
        if not tags_list:
            return Response({'msg': '视频未设置标签', 'success': False}, status.HTTP_200_OK)
        index = random.randint(0, tags_list.count()-1)
        tags = Tags.objects.filter(id=tags_list[index].id).first()
        video_list = tags.basevideo_set.all()
        if video_list.count() <= limit:
            rows = BaseVideoSerializer(video_list, many=True).data
        else:
            start = random.randint(0, video_list.count()-limit)
            rows = BaseVideoSerializer(video_list[start, limit], many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': rows
        }
        return Response(result, status.HTTP_200_OK)
