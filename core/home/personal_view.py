# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/3/2 19:07
# @Author  : NoWords
# @FileName: personal_view.py
from ..serializers import UserTravelSerializer, UserSerializer
from ..models import UserTravel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

import logging

logger = logging.getLogger(__name__)


class OperationHistoryApiView(APIView):

    def get(self, request, *args, **kwargs):
        params = request.GET
        user_id = params.get('userId')
        video_id = params.get('videoId')
        discover_id = params.get('discoverId')
        operation = params.get('operation')
        page_size = params.get('pageSize')
        page_no = params.get('pageNo')
        filters = {}
        if user_id:
            filters['user_id'] = user_id
        if video_id:
            filters['video_id'] = video_id
        if discover_id:
            filters['discover_id'] = discover_id
        if operation:
            filters['operation'] = operation
        user_travel = UserTravel.objects.filter(**filters).order_by('-id')
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = UserTravelSerializer(user_travel[start:end], many=True).data
        else:
            rows = UserTravelSerializer(user_travel, many=True).data
        result = {
            'msg': '添加数据成功',
            'success': True,
            'data': {
                'total': user_travel.count(),
                'rows': rows
            }
        }
        return Response(result, status.HTTP_200_OK)


class UserInfoApiView(APIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.user.id).first()
        result = {
            'msg': '添加数据成功',
            'success': True,
            'data': UserSerializer(data=user).data
        }
        return Response(result, status.HTTP_200_OK)
