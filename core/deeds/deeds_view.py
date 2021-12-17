# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 12:59
# @Author  : NoWords
# @FileName: deeds_view.py
from ..serializers import DeedsSerializer
from ..models import Deeds
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class DeedsAPIView(APIView):
    """
    活动管理
    """

    def get(self, request, *args, **kwargs):
        """
        获取活动列表
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        deeds_id = data.get('id')
        title = data.get('title')
        content = data.get('content')
        sort = data.get('sort')
        filters = {'is_delete': 0}
        if deeds_id:
            filters['id'] = deeds_id
        if title:
            filters['title__contains'] = title
        if content:
            filters['content__contains'] = content
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Deeds.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Deeds.objects.filter(**filters).order_by(*sort_list)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': DeedsSerializer(rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        新增活动
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
        serializer = DeedsSerializer(data=data, partial=True)
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
        修改活动
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.data
        data['updater_id'] = request.user.id
        data['updater_name'] = request.user.username
        deeds_id = data.get('id')
        deeds = Deeds.objects.filter(id=deeds_id).first()
        if not deeds:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = DeedsSerializer(deeds, data=data, partial=True)
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
        删除活动
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.GET
        deeds_id = data.get('id')
        deeds = Deeds.objects.get(id=deeds_id)
        if not deeds:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        deeds.is_delete = True
        deeds.save()
        return Response({
            'msg': '删除活动成功',
            'success': True,
            'data': DeedsSerializer(deeds).data
        }, status.HTTP_200_OK)
