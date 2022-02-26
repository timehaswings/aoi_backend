# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/2/26 9:24
# @Author  : nowords
# @FileName: recommend_view.py

from ..models import Category, Tags, Area, BaseVideo
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
            return Response({msg: '参数错误', success: False}, status.HTTP_200_OK)
        video = BaseVideo.objects.filter(id=vid, is_delete=0, is_active=1).first()
        if not video:
            return Response({msg: '视频未找到', success: False}, status.HTTP_200_OK)
        print(video.tags)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': []
        }
        return Response(result, status.HTTP_200_OK)
