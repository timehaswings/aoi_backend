# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 15:06
# @Author  : NoWords
# @FileName: config_view.py
from core.common.common_view import CommonAPIView
from core.models import Config
from core.serializers import ConfigSerializer


class ConfigAPIView(CommonAPIView):
    """
    配置管理
    """

    model = Config
    serializer = ConfigSerializer
    add_insert_creator = True
    update_insert_updater = True
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'name__contains', 'request_key': 'name'},
        {'filter_key': 'codename', 'request_key': 'codename'},
    ]
