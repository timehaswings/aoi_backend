# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/7/30 19:04
# @Author  : NoWords
# @FileName: views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_captcha.serializers import RestCaptchaSerializer
from rest_framework_jwt.settings import api_settings

from core.utils import catch_except
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


class RegisterAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    @catch_except
    def post(self, request, *args, **kwargs):
        """
        用户注册
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        username = data.get('username')
        password = data.get('password')
        captcha = RestCaptchaSerializer(data=data)
        if not captcha.is_valid():
            return Response({
                'msg': '验证码错误',
                'success': False
            }, status.HTTP_200_OK)
        user = User.objects.filter(Q(username=username) | Q(email=username)).first()
        if user:
            return Response({
                'msg': '该账户已存在',
                'success': False
            }, status.HTTP_200_OK)
        if '@' not in username:
            return Response({
                'msg': '邮箱格式错误',
                'success': False
            }, status.HTTP_200_OK)
        email = username
        username = email.split('@')[0]
        user = User.objects.create_user(username=username, password=password, email=email)
        # 创建token，注册即登录
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            'msg': '添加成功',
            'success': True,
            'data': {
                'token': token,
                'user': UserSerializer(user).data
            }
        }, status.HTTP_200_OK)
