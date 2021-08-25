# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/2 12:10
# @Author  : NoWords
# @FileName: middleware.py
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status

import logging

logger = logging.getLogger(__name__)


class ExpHandlerMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        """
        统一异常处理
        :param request:
        :param exception:
        :return:
        """
        message = 'path: %s, method: %s, error: %s' % (request.path, request.method, exception)
        logger.error(message)
        result = {'msg': message, 'success': False}
        return JsonResponse(data=result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
