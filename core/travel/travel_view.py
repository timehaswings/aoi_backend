# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 11:38
# @Author  : NoWords
# @FileName: travel_view.py
from ..serializers import UserTravelSerializer
from ..models import UserTravel
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)


class UserTravelAPIView(APIView):
    """
    用户轨迹管理
    """

    model = UserTravel
    serializer = UserTravelSerializer
    query = [
        {'filter_key': 'id', 'request_key': 'id'},
        {'filter_key': 'operation', 'request_key': 'operation'},
    ]
