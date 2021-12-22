# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/18 10:46
# @Author  : NoWords
# @FileName: permission_view.py

from core.common.common_view import CommonAPIView
from django.contrib.auth.models import Permission

from core.serializers import PermissionSerializer


class PermissionAPIView(CommonAPIView):
    """
    权限管理
    """

    model = Permission
    serializer = PermissionSerializer
    filters = None
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
    ]

    def post(self, request, *args, **kwargs):
        return self.not_implements()

    def put(self, request, *args, **kwargs):
        return self.not_implements()

    def delete(self, request, *args, **kwargs):
        return self.not_implements()