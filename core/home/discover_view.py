# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/18 12:32
# @Author  : NoWords
# @FileName: discover_view.py

from core.serializers import DiscoverSerializer
from ..models import Discover
from ..common.unlimited_data_view import UnlimitedDataView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class DiscoverApiView(UnlimitedDataView):

    def get(self, request, *args, **kwargs):
        params = request.GET
        page_size = params.get('pageSize')
        page_no = params.get('pageNo')
        filters = {'is_active': True}
        if params.get('id'):
            filters['id'] = params.get('id')
        if params.get('name'):
            filters['name__contains'] = params.get('name')
        if params.get('content'):
            filters['content__contains'] = params.get('content')
        discover = Discover.objects.filter(**filters).order_by('sort,-id')
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = DiscoverSerializer(discover[start:end], many=True).data
        else:
            rows = DiscoverSerializer(discover, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'total': discover.count(),
                'rows': rows
            }
        }
        return Response(result, status.HTTP_200_OK)
