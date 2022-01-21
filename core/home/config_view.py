# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2022/1/18 10:08
# @Author  : NoWords
# @FileName: config_view.py
from ..serializers import ConfigSerializer
from ..models import Config
from ..common.unlimited_data_view import UnlimitedDataView


class ConfigApiView(UnlimitedDataView):
    serializer = ConfigSerializer
    model = Config
    filters = {'is_delete': 0}

