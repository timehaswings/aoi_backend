# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/18 10:08
# @Author  : NoWords
# @FileName: config_view.py
from ..serializers import ConfigSerializer
from ..models import Config
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class ConfigApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        configs = Config.objects.filter(is_delete=0).order_by('-id')
        configs = ConfigSerializer(configs, many=True).data
        result = {
            'msg': '获取成功',
            'success': True,
            'data': configs
        }
        return Response(result, status.HTTP_200_OK)

