# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/30 9:08
# @Author  : NoWords
# @FileName: urls.py
from django.urls import re_path

from .base.base_consumer import BaseConsumer

urlpatterns = [
    re_path(r'api/v1/ws/base', BaseConsumer.as_asgi()),
]
