# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/18 12:26
# @Author  : NoWords
# @FileName: category_view.py

from ..serializers import CategorySerializer, TagsSerializer, AreaSerializer, BaseVideoSerializer
from ..models import Category, Tags, Area, BaseVideo
from ..common.unlimited_data_view import UnlimitedDataView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CategoryApiView(UnlimitedDataView):
    serializer = CategorySerializer
    model = Category
    sort = 'sort'
    filters = {'is_delete': 0, 'is_active': 1}


class TagsApiView(UnlimitedDataView):
    serializer = TagsSerializer
    model = Tags
    sort = 'sort'
    filters = {'is_delete': 0, 'is_active': 1}


class AreaApiView(UnlimitedDataView):
    serializer = AreaSerializer
    model = Area
    sort = 'sort'


class VideoApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        filters = {'is_delete': 0, 'is_active': 1}
        params = request.GET
        page_size = params.get('pageSize')
        page_no = params.get('pageNo')
        keyword = params.get('keyword')
        sort_list = ['-sort']
        if params.get('category_id'):
            filters['category_id'] = params.get('category_id')
        if params.get('tag_ids'):
            filters['tags_id__in'] = params.get('tag_ids').split(',')
        if params.get('sort'):
            sort_list = params.get('sort').split(',')
        model = BaseVideo.objects.filter(**filters)
        if keyword:
            model = model.filter(Q(name__contains=keyword) | Q(desc__contains=keyword) | Q(artists__contains=keyword))
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = model.order_by(*sort_list)[start:end]
        else:
            rows = model.order_by(*sort_list)
        rows = BaseVideoSerializer(rows, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'total': model.count(),
                'rows': rows
            }
        }
        return Response(result, status.HTTP_200_OK)
