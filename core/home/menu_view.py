# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/26 10:04
# @Author  : NoWords
# @FileName: menu_view.py
from ..serializers import MenuSerializer, ConfigSerializer
from ..models import Menu, Config
from ..menu.menu_view import convert_public_tree, convert_private_tree
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class PublicMenuApiView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        filters = {'is_delete': 0}
        menus = Menu.objects.filter(**filters).order_by('parent_id', 'sort')
        menus = MenuSerializer(menus, many=True).data
        menu_tree = convert_public_tree(menus)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': menu_tree
        }
        return Response(result, status.HTTP_200_OK)


class PrivateMenuApiView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            filters = {'is_delete': 0}
            menus = Menu.objects.filter(**filters).order_by('parent_id', 'sort')
            menus = MenuSerializer(menus, many=True).data
            menu_tree = convert_private_tree(menus)
        else:
            menu_tree = []
        result = {
            'msg': '获取成功',
            'success': True,
            'data': menu_tree
        }
        return Response(result, status.HTTP_200_OK)
