# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/25 10:15
# @Author  : NoWords
# @FileName: base_video_view.py
from core.common.common_view import CommonAPIView
from core.models import BaseVideo
from core.serializers import BaseVideoSerializer
from rest_framework.response import Response
from rest_framework import status
import uuid
import logging

logger = logging.getLogger(__name__)


class BaseVideoAPIView(CommonAPIView):
    """
    视频管理
    """

    model = BaseVideo
    serializer = BaseVideoSerializer
    add_insert_creator = True
    update_insert_updater = True
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'is_active', 'request_key': 'isActive', 'type': 'boolean'},
        {'filter_key': 'name__contains', 'request_key': 'name'},
    ]

    def post(self, request, *args, **kwargs):
        """
        视频管理-新增
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        data['create_id'] = request.user.id
        data['updater_id'] = data['create_id']
        data['create_name'] = request.user.username
        data['updater_name'] = data['create_name']
        data['guid'] = str(uuid.uuid1().int)
        serializer = BaseVideoSerializer(data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '新增失败：%s' % e,
                'success': False
            }, status.HTTP_200_OK)
        return Response({
            'msg': '新增成功',
            'success': True,
            'data': serializer.data
        }, status.HTTP_200_OK)

