# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 11:38
# @Author  : NoWords
# @FileName: travel_view.py
from core.common.common_view import CommonAPIView
from ..serializers import UserTravelSerializer
from ..models import UserTravel, BaseVideo, Discover
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class UserTravelAPIView(CommonAPIView):
    """
    用户轨迹管理
    """

    model = UserTravel
    serializer = UserTravelSerializer
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'operation', 'request_key': 'operation'},
    ]

    def post(self, request, *args, **kwargs):
        data = request.data
        video_id = data.get('video_id')
        user_id = data.get('user_id')
        discover_id = data.get('discover_id')
        if not user_id:
            return Response({'msg': '参数错误', 'success': False}, status.HTTP_200_OK)
        user = User.objects.filter(id=user_id).first()
        if video_id:
            video = BaseVideo.objects.filter(id=video_id, is_delete=0, is_active=1).first()
            user_travel = UserTravel.objects.create(user=user, video=video, **data)
        elif discover_id:
            discover = Discover.objects.filter(id=discover_id, is_delete=0, is_active=1).first()
            user_travel = UserTravel.objects.create(user=user, discover=discover, **data)
        else:
            return Response({'msg': '参数错误', 'success': False}, status.HTTP_200_OK)
        result = {
            'msg': '添加数据成功',
            'success': True,
            'data': UserTravelSerializer(user_travel).data
        }
        return Response(result, status.HTTP_200_OK)
