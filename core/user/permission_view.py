# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 10:46
# @Author  : NoWords
# @FileName: permission_view.py

from django.contrib.auth.models import Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import PermissionSerializer
import logging

logger = logging.getLogger(__name__)


class PermissionAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        获取权限列表
        :param request:
        :param args:
        :param kwargs:
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
            rows = Permission.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = Permission.objects.filter(**filters).order_by(*sort_list)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'rows': PermissionSerializer(rows, many=True).data,
                'total': rows.count()
            }
        }
        return Response(result, status.HTTP_200_OK)
