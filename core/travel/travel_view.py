# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 11:38
# @Author  : NoWords
# @FileName: travel_view.py
from ..serializers import UserTravelSerializer
from ..models import UserTravel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class UserTravelAPIView(APIView):
    """
    用户轨迹管理
    """

    def get(self, request, *args, **kwargs):
        """
        获取用户轨迹列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        user_travel_id = data.get('id')
        operation = data.get('operation')
        filters = {'is_delete': 0}
        if user_travel_id:
            filters['id'] = user_travel_id
        if operation:
            filters['operation'] = operation
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = UserTravel.objects.filter(**filters)[start:end]
        else:
            rows = UserTravel.objects.filter(**filters)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': UserTravelSerializer(rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        新增数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        serializer = UserTravelSerializer(data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '添加失败：%s' % e,
                'success': False
            }, status.HTTP_200_OK)
        return Response({
            'msg': '添加成功',
            'success': True
        }, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        修改数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        user_travel_id = data.get('id')
        user_travel = UserTravel.objects.filter(id=user_travel_id).first()
        if not user_travel:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = UserTravelSerializer(user_travel, data=data, partial=True)
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
            'success': True
        }, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        删除数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        user_travel_id = data.get('id')
        user_travel = UserTravel.objects.get(id=user_travel_id)
        if not user_travel:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        user_travel.is_delete = True
        user_travel.save()
        return Response({
            'msg': '删除用户轨迹成功',
            'success': True,
            'data': UserTravelSerializer(user_travel).data
        }, status.HTTP_200_OK)
