# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 9:02
# @Author  : NoWords
# @FileName: group_menu_view.py
from core.models import GroupMenu, Menu
from django.contrib.auth.models import Group, User
from core.serializers import GroupMenuSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging

logger = logging.getLogger(__name__)


class GroupMenuAPIView(APIView):

    def post(self, request, format=None):
        """
        添加组别与菜单关联
        :param request:
        :param format:
        :return:
        """
        data = request.data
        group_id = data.get('group_id')
        menu_id = data.get('menu_id')
        group = Group.objects.filter(id=group_id).first()
        menu = Menu.objects.filter(id=menu_id, is_delete=0).first()
        if not group or not menu:
            return Response({
                'msg': '组别或菜单不存在',
                'success': False,
            }, status.HTTP_200_OK)
        GroupMenu.objects.create(group_id=group_id, menu_id=menu_id)
        return Response({
            'msg': '添加关联成功',
            'success': True
        }, status.HTTP_200_OK)


class UserMenuAPIView(APIView):

    def get(self, request, format=None):
        """
        获取用户拥有的菜单
        :param request:
        :param format:
        :return:
        """
        user_id = request.user.id
        user = User.objects.filter(id=user_id).first()
        if not user:
            return Response({
                'msg': '用户不存在',
                'success': False,
            }, status.HTTP_200_OK)
        group_ids = Group.objects.filter(id__in=user.groups.all()).values_list('id', flat=True)
        if not group_ids:
            return Response({
                'msg': '用户尚未关联组别',
                'success': False,
            }, status.HTTP_200_OK)
        group_menu = GroupMenu.objects.filter(group__in=group_ids)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': GroupMenuSerializer(group_menu, many=True).data,
        }
        return Response(result, status.HTTP_200_OK)