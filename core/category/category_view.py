# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/25 10:05
# @Author  : NoWords
# @FileName: category_view.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from ..serializers import CategorySerializer
from ..models import Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CategoryAPIView(APIView):
    """
    分类管理
    """

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization", ))
    def get(self, request, *args, **kwargs):
        """
        获取分类列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        filters = {}
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        category_id = data.get('id')
        is_active = data.get('isActive')
        name = data.get('name')
        sort = data.get('sort')
        if category_id:
            filters['id'] = category_id
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
            rows = Category.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Category.objects.filter(**filters).order_by(*sort_list)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': CategorySerializer(rows, many=True).data, 'total': rows.count()}
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
        serializer = CategorySerializer(obj, data=data, partial=True)
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
        category_id = data.get('id')
        obj = Category.objects.filter(id=category_id).first()
        if obj:
            serializer = CategorySerializer(obj, data=data, partial=True)
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
        category_id = data.get('id')
        u = Category.objects.get(id=category_id)
        u.delete()
        return Response({
            'msg': '删除用户成功',
            'success': True,
            'data': CategorySerializer(u).data
        }, status.HTTP_200_OK)
