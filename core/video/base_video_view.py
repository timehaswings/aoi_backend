# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/25 10:15
# @Author  : NoWords
# @FileName: base_video_view.py
from rest_framework.views import APIView
from core.models import BaseVideo
from core.serializers import BaseVideoSerializer
from rest_framework.response import Response
from rest_framework import status
import uuid
import logging

logger = logging.getLogger(__name__)


class BaseVideoAPIView(APIView):

    def get(self, request, format=None):
        """
        视频管理-查询
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        is_active = data.get('isActive')
        name = data.get('name')
        sort = data.get('sort')
        video_id = data.get('id')
        filters = {'is_delete': False}
        if video_id:
            filters['id'] = video_id
        if is_active:
            filters['is_active'] = is_active
        if name:
            filters['name__contains'] = name
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = BaseVideo.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = BaseVideo.objects.filter(**filters).order_by(*sort_list)
        total = rows.count()
        rows = BaseVideoSerializer(rows, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'rows': rows,
                'total': total
            }
        }
        return Response(result, status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        视频管理-新增
        :param request:
        :param format:
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

    def put(self, request, format=None):
        """
        修改数据
        :param request:
        :param format:
        :return:
        """
        data = request.data
        data['updater_id'] = request.user.id
        data['updater_name'] = request.user.username
        video = BaseVideo.objects.filter(id=data.get('id')).first()
        if not video:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = BaseVideoSerializer(video, data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '修改失败：%s' % e,
                'success': False
            }, status.HTTP_200_OK)
        return Response({
            'msg': '修改成功',
            'success': True,
            'data': serializer.data
        }, status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        删除数据
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        video_id = data.get('id')
        video = BaseVideo.objects.get(id=video_id)
        if not video:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        video.is_delete = True
        video.save()
        return Response({
            'msg': '删除视频成功',
            'success': True,
            'data': BaseVideoSerializer(video).data
        }, status.HTTP_200_OK)
