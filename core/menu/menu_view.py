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


def recursion_menu(menus, menu, require_login):
    if not menus or not menu:
        return
    for sub_menu in menus:
        if sub_menu['parent_id'] == menu['id']:
            if 'children' in menu.keys():
                if require_login is None:
                    menu['children'].append(sub_menu)
                elif require_login:
                    menu['children'].append(sub_menu)
            else:
                if require_login is None:
                    menu['children'] = [sub_menu]
                elif require_login:
                    menu['children'] = [sub_menu]
            recursion_menu(menus, sub_menu, require_login)


def convert_menu_tree(menus, require_login=None):
    menu_tree = []
    for menu in menus:
        if menu['parent_id'] == -1:
            if require_login is not None and not require_login:
                break
            menu_tree.append(menu)
            recursion_menu(menus, menu, require_login)
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
        filters = {'is_delete': 0}
        menus = Menu.objects.filter(**filters).order_by('parent_id', 'sort')
        menus = MenuSerializer(menus, many=True).data
        menu_tree = convert_menu_tree(menus)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': menu_tree
        }
        return Response(result, status.HTTP_200_OK)
