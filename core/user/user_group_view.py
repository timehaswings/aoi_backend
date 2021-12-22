# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 11:38
# @Author  : Nowords
# @FileName: user_group_view.py

from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import GroupSerializer
import logging

logger = logging.getLogger(__name__)


class UserGroupAPIView(APIView):

    def get(self, request, format=None):
        """
        获取用户所属组别
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        user_id = data.get('userId')
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({
                'msg': '用户不存在',
                'success': False,
            }, status.HTTP_200_OK)
        groups = Group.objects.filter(id__in=user.groups.all())
        result = {
            'msg': '获取成功',
            'success': True,
            'data': GroupSerializer(groups, many=True).data,
        }
        return Response(result, status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        为用户添加组别
        :param request:
        :param format:
        :return:
        """
        data = request.data
        user_id = data.get('user_id')
        group_ids = data.get('group_ids')
        group_id_list = group_ids.split(',')
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({
                'msg': '用户不存在',
                'success': False,
            }, status.HTTP_200_OK)
        if group_id_list:
            groups = Group.objects.filter(id__in=group_id_list)
            user.groups.set(groups)
        else:
            groups = []
            user.groups.clear()
        result = {
            'msg': '获取成功',
            'success': True,
            'data': GroupSerializer(groups, many=True).data,
        }
        return Response(result, status.HTTP_200_OK)
