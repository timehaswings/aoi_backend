# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 15:06
# @Author  : NoWords
# @FileName: config_view.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from core.models import Config
from core.serializers import ConfigSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class ConfigAPIView(APIView):
    """
    配置管理视图
    """

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization", ))
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
        codename = data.get('codename')
        site_id = data.get('id')
        filters = {}
        if site_id:
            filters['id'] = site_id
        if codename:
            filters['codename'] = codename
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Config.objects.filter(**filters)[start:end]
        else:
            rows = Config.objects.filter(**filters)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'rows': ConfigSerializer(rows, many=True).data,
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
        serializer = ConfigSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
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
        config_id = data.get('id')
        obj = Config.objects.filter(id=config_id).first()
        if obj:
            del data['id']
            serializer = ConfigSerializer(obj, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
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
        config_id = data.get('id')
        u = Config.objects.get(id=config_id)
        u.delete()
        return Response({
            'msg': '删除成功',
            'success': ConfigSerializer(u).data
        }, status.HTTP_200_OK)