# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/28 8:56
# @Author  : NoWords
# @FileName: discover_view.py
from ..serializers import DiscoverSerializer
from ..models import Discover
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class DiscoverAPIView(APIView):
    """
    发现管理
    """

    def get(self, request, *args, **kwargs):
        """
        获取发现列表
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        discover_id = data.get('id')
        is_active = data.get('isActive')
        name = data.get('name')
        content = data.get('content')
        sort = data.get('sort')
        filters = {'is_delete': False}
        if discover_id:
            filters['id'] = discover_id
        if name:
            filters['name__contains'] = name
        if content:
            filters['content__contains'] = content
        if is_active:
            filters['is_active'] = is_active
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Discover.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Discover.objects.filter(**filters).order_by(*sort_list)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': DiscoverSerializer(rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        新增发现
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
        serializer = DiscoverSerializer(data=data, partial=True)
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
        修改发现
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.data
        data['updater_id'] = request.user.id
        data['updater_name'] = request.user.username
        discover_id = data.get('id')
        discover = Discover.objects.filter(id=discover_id).first()
        if not discover:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = DiscoverSerializer(discover, data=data, partial=True)
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
        删除发现
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.GET
        discover_id = data.get('id')
        discover = Discover.objects.get(id=discover_id)
        if not discover:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        discover.is_delete = True
        discover.save()
        return Response({
            'msg': '删除发现成功',
            'success': True,
            'data': DiscoverSerializer(discover).data
        }, status.HTTP_200_OK)
