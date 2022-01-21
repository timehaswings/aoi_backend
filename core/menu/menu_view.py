# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/25 10:04
# @Author  : NoWords
# @FileName: menu_view.py
from core.common.common_view import CommonAPIView
from ..serializers import MenuSerializer
from ..models import Menu

from rest_framework.response import Response
from rest_framework import status


def recursion_menu(menus, menu):
    if not menus or not menu:
        return
    for sub_menu in menus:
        if sub_menu['parent_id'] == menu['id']:
            if 'children' in menu.keys():
                menu['children'].append(sub_menu)
            else:
                menu['children'] = [sub_menu]
            recursion_menu(menus, sub_menu)


def convert_menu_tree(menus):
    menu_tree = []
    for menu in menus:
        if menu['parent_id'] == -1:
            menu_tree.append(menu)
            recursion_menu(menus, menu)
    return menu_tree


def convert_public_tree(menus):
    menu_tree = []
    for menu in menus:
        if menu['id'] == 2:
            menu_tree.append(menu)
            recursion_menu(menus, menu)
    return menu_tree


def convert_private_tree(menus):
    menu_tree = []
    for menu in menus:
        if menu['id'] == 3:
            menu_tree.append(menu)
            recursion_menu(menus, menu)
    return menu_tree


class MenuAPIView(CommonAPIView):
    """
    菜单管理
    """

    model = Menu
    serializer = MenuSerializer
    add_insert_creator = True
    update_insert_updater = True

    def get(self, request, *args, **kwargs):
        """
        获取菜单树
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        require_login = data.get('requireLogin')
        filters = {'is_delete': 0}
        if require_login:
            filters['require_login'] = require_login
        menus = Menu.objects.filter(**filters).order_by('parent_id', 'sort')
        menus = MenuSerializer(menus, many=True).data
        menu_tree = convert_menu_tree(menus)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': menu_tree
        }
        return Response(result, status.HTTP_200_OK)
