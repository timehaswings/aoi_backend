# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 9:02
# @Author  : NoWords
# @FileName: group_view.py

from django.contrib.auth.models import Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import GroupSerializer
import logging

logger = logging.getLogger(__name__)


class GroupAPIView(APIView):
    """
    组别管理视图
    """
    def get(self, request, format=None):
        """
        查询数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        sort = data.get('sort')
        group_id = data.get('id')
        filters = {}
        if group_id:
            filters['id'] = group_id
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Group.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Group.objects.filter(**filters).order_by(*sort_list)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'rows': GroupSerializer(rows, many=True).data,
                'total': rows.count()
            }
        }
        return Response(result, status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        新增数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.data
        serializer = GroupSerializer(data=data, partial=True)
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
            'success': True,
        }, status.HTTP_200_OK)

    def put(self, request, format=None):
        """
        修改数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.data
        group_id = data.get('id')
        site = Group.objects.filter(id=group_id).first()
        if not site:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = GroupSerializer(site, data=data, partial=True)
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
        }, status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        删除数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        group_id = data.get('id')
        site = Group.objects.get(id=group_id)
        if not site:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        site.delete()
        return Response({
            'msg': '删除成功',
            'success': GroupSerializer(site).data
        }, status.HTTP_200_OK)

