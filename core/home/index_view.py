# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/18 10:26
# @Author  : NoWords
# @FileName: index_view.py

from ..serializers import BaseVideoSerializer, CategorySerializer
from ..models import BaseVideo, Category
from random import randint
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CarouselApiView(APIView):
    """
    主页轮播数据
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        filters = {'is_delete': 0, }
        count = BaseVideo.objects.filter(**filters).count()
        limit = 6  # 数据量
        if count <= limit:
            base_video = BaseVideo.objects.filter(**filters)
        else:
            start = randint(0, count - limit)
            base_video = BaseVideo.objects.filter(**filters)[start: start + limit]
        base_video = BaseVideoSerializer(base_video, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': base_video
        }
        return Response(result, status.HTTP_200_OK)


class CategoryVideoApiView(APIView):
    """
    主页分类数据
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        # 获取随机分类
        category_filters = {'is_delete': 0}
        category_count = Category.objects.filter(**category_filters).count()
        category_limit = 5
        if category_count <= category_limit:
            category = Category.objects.filter(**category_filters)
        else:
            start = randint(0, category_count - category_limit)
            category = Category.objects.filter(**category_filters)[start: start + category_limit]
        category = CategorySerializer(category, many=True).data
        # 获取分类下的视频
        video_limit = 8
        for item in category:
            video_filter = {'category_id': item['id'], 'is_delete': 0}
            video_count = BaseVideo.objects.filter(**video_filter).count()
            print(video_count)
            if video_count <= video_limit:
                base_video = BaseVideo.objects.filter(**video_filter)
            else:
                start = randint(0, video_count - video_limit)
                base_video = BaseVideo.objects.filter(**video_filter)[start: start + video_limit]
            base_video = BaseVideoSerializer(base_video, many=True).data
            item['video_list'] = base_video
        result = {
            'msg': '获取成功',
            'success': True,
            'data': category
        }
        return Response(result, status.HTTP_200_OK)
