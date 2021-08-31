# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/25 10:04
# @Author  : NoWords
# @FileName: tags_view.py
from ..serializers import TagsSerializer
from ..models import Tags
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class TagsAPIView(APIView):
    """
    标签管理
    """

    def get(self, request, *args, **kwargs):
        """
        获取标签列表
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.GET
        filters = {'is_delete': False}
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        tags_id = data.get('id')
        is_active = data.get('isActive')
        name = data.get('name')
        sort = data.get('sort')
        if tags_id:
            filters['id'] = tags_id
        if name:
            filters['name__contains'] = name
        if is_active:
            filters['is_active'] = is_active
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Tags.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Tags.objects.filter(**filters).order_by(*sort_list)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': TagsSerializer(rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        新增标签
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
        serializer = TagsSerializer(data=data, partial=True)
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
        修改标签
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.data
        data['updater_id'] = request.user.id
        data['updater_name'] = request.user.username
        tags_id = data.get('id')
        tags = Tags.objects.filter(id=tags_id).first()
        if not tags:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = TagsSerializer(tags, data=data, partial=True)
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
        删除标签
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """
        data = request.GET
        tags_id = data.get('id')
        tags = Tags.objects.get(id=tags_id)
        if not tags:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        tags.is_delete = True
        tags.save()
        return Response({
            'msg': '删除标签成功',
            'success': True,
            'data': TagsSerializer(tags).data
        }, status.HTTP_200_OK)
