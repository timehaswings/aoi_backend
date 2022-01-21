# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/21 9:11
# @Author  : NoWords
# @FileName: unlimited_data_view.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class UnlimitedDataView(APIView):
    permission_classes = []
    authentication_classes = []
    filters = {}
    model = None
    serializer = None
    sort = '-id'

    def get(self, request, *args, **kwargs):
        if not self.model or not self.serializer:
            return Response({'msg': '未配置模型或者序列化器', 'success': False}, status.HTTP_200_OK)
        data = self.model.objects.filter(**self.filters).order_by(self.sort)
        data = self.serializer(data, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': data
        }
        return Response(result, status.HTTP_200_OK)
