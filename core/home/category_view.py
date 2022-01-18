# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/18 12:26
# @Author  : NoWords
# @FileName: category_view.py

from ..serializers import CategorySerializer, TagsSerializer
from ..models import Category, Tags
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CategoryApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        filters = {'is_delete': 0, 'is_active': 1}
        category = Category.objects.filter(**filters).order_by('sort')
        category = CategorySerializer(category, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': category
        }
        return Response(result, status.HTTP_200_OK)


class TagsApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        filters = {'is_delete': 0, 'is_active': 1}
        tags = Tags.objects.filter(**filters).order_by('sort')
        tags = TagsSerializer(tags, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': tags
        }
        return Response(result, status.HTTP_200_OK)


class ApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        filters = {'is_delete': 0, 'is_active': 1}

        result = {
            'msg': '获取成功',
            'success': True,
            'data': []
        }
        return Response(result, status.HTTP_200_OK)
