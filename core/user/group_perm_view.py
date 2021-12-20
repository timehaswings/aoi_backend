# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 10:51
# @Author  : NoWords
# @FileName: group_perm_view.py

from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.serializers import PermissionSerializer
import logging

logger = logging.getLogger(__name__)


class GroupPermAPIView(APIView):

    def get(self, request, format=None):
        data = request.GET
        group_id = data.get('groupId')
        group = Group.objects.filter(id=group_id).first()
        if not group:
            return Response({
                'msg': '组别不存在',
                'success': False,
            }, status.HTTP_200_OK)
        permissions = Permission.objects.filter(id__in=group.permissions.all())
        result = {
            'msg': '设置成功',
            'success': True,
            'data': PermissionSerializer(permissions, many=True).data,
        }
        return Response(result, status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        为组别添加权限
        :param request:
        :param format:
        :return:
        """
        data = request.data
        group_id = data.get('group_id')
        permission_ids = data.get('permission_ids')
        permission_id_list = permission_ids.split(',')
        group = Group.objects.filter(id=group_id).first()
        if not group:
            return Response({
                'msg': '设置权限失败',
                'success': False,
            }, status.HTTP_200_OK)
        if permission_id_list:
            permissions = Permission.objects.filter(id__in=permission_id_list)
            group.permissions.set(permissions)
        else:
            permissions = []
            group.permissions.clear()
        result = {
            'msg': '设置成功',
            'success': True,
            'data': PermissionSerializer(permissions, many=True).data,
        }
        return Response(result, status.HTTP_200_OK)
