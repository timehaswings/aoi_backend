# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/7/30 19:04
# @Author  : NoWords
# @FileName: user_view.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from ..serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class UserAPIView(APIView):
    """
    用户管理视图
    """
    def get(self, request, *args, **kwargs):
        """
        获取用户列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        filters = {}
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        sort = data.get('sort')
        user_id = data.get('id')
        username = data.get('username')
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        is_active = data.get('is_active')
        is_staff = data.get('is_staff')
        if user_id:
            filters['id'] = user_id
        if username:
            filters['username__contains'] = username
        if first_name:
            filters['first_name__contains'] = first_name
        if last_name:
            filters['last_name__contains'] = last_name
        if email:
            filters['email__contains'] = email
        if is_active:
            filters['is_active'] = is_active
        if is_staff:
            filters['is_staff'] = is_staff
        if sort:
            sort_list = sort.split(',')
        else:
            sort_list = ['-id']
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = User.objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = User.objects.filter(**filters).order_by(*sort_list)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': UserSerializer(rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        添加用户
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        email = data.get('email')
        password = data.get('password')
        if not email or not password:
            return Response({
                'msg': '必须存在邮箱和密码',
                'success': False
            }, status.HTTP_200_OK)
        username = email.split('@')[0]
        user = User.objects.filter(username=username).first()
        if user:
            if user.email == email:
                return Response({
                    'msg': '当前邮箱已被注册',
                    'success': False
                }, status.HTTP_200_OK)
            else:
                username = username + '~'
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({
            'msg': '添加成功',
            'success': True,
            'data': UserSerializer(user).data
        }, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        修改用户
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        user_id = data.get('id')
        obj = User.objects.filter(id=user_id).first()
        if not obj:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        if data.get('password'):
            return Response({
                'msg': '不可修改密码',
                'success': False
            }, status.HTTP_200_OK)
        serializer = UserSerializer(obj, data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '修改失败：%s' % e,
                'success': False
            }, status.HTTP_200_OK)
        return Response({
            'msg': '修改成功',
            'success': True
        }, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """
        删除用户
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        user_id = data.get('id')
        user = User.objects.get(id=user_id)
        if not user:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        user.delete()
        return Response({
            'msg': '删除用户成功',
            'success': True,
            'data': UserSerializer(user).data
        }, status.HTTP_200_OK)


class PasswordAPIView(APIView):

    def put(self, request, *args, **kwargs):
        """
        用户修改密码
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        username = data.get('username')
        old_password = data.get('oldPassword')
        new_password = data.get('newPassword')
        if not username or not old_password or not new_password:
            return Response({
                'msg': '参数缺失',
                'success': False
            }, status.HTTP_200_OK)
        user = authenticate(username=username, password=old_password)
        if user is None:
            return Response({
                'msg': '用户原始密码错误',
                'success': False
            }, status.HTTP_200_OK)
        user.set_password(new_password)
        user.save()
        return Response({
            'msg': '修改密码成功',
            'success': True
        }, status.HTTP_200_OK)

