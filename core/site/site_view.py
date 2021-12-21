# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 9:52
# @Author  : NoWords
# @FileName: site_view.py
from core.common.common_view import CommonAPIView
from django.contrib.sites.models import Site

from core.serializers import SiteSerializer
import logging

logger = logging.getLogger(__name__)


class SiteAPIView(CommonAPIView):
    """
    站点管理视图
    """
    model = Site
    serializer = SiteSerializer
    filters = None
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
    ]
