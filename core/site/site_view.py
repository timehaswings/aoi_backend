# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 9:52
# @Author  : NoWords
# @FileName: site_view.py
from django.contrib.sites.models import Site
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import SiteSerializer
import logging

logger = logging.getLogger(__name__)


class SiteAPIView(APIView):
    """
    站点管理视图
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
        sort = data.get('sort')
        site_id = data.get('id')
        filters = {}
        if site_id:
            filters['id'] = site_id
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Site.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Site.objects.filter(**filters).order_by(*sort_list)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'rows': SiteSerializer(rows, many=True).data,
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
        serializer = SiteSerializer(data=data)
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
        site_id = data.get('id')
        obj = Site.objects.filter(id=site_id).first()
        if obj:
            serializer = SiteSerializer(obj, data=data, partial=True)
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
        site_id = data.get('id')
        u = Site.objects.get(id=site_id)
        u.delete()
        return Response({
            'msg': '删除成功',
            'success': SiteSerializer(u).data
        }, status.HTTP_200_OK)
