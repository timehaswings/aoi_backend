# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 13:02
# @Author  : NoWords
# @FileName: utils.py
from rest_framework.response import Response
from rest_framework import status
from core.serializers import UserSerializer
import sys
import os
import logging

logger = logging.getLogger(__name__)


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User
    """
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


def catch_except(func):
    """
    统一异常捕获装饰器
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error('服务器内部错误：%s，文件：%s，代码行：%s' % (e, file_name, exc_tb.tb_lineno))
            return Response({
                'msg': '%s' % e,
                'success': False
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    return wrapper
