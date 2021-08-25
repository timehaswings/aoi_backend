# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/7/30 19:04
# @Author  : NoWords
# @FileName: user_view.py
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from ..serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class UserAPIView(APIView):

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization", ))
    def get(self, request, *args, **kwargs):
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

    # 添加用户信息
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg': '添加成功',
            'success': True
        }, status.HTTP_200_OK)

    # 修改用户信息
    def put(self, request, *args, **kwargs):
        data = request.data
        user_id = data.get('id')
        obj = User.objects.filter(id=user_id).first()
        if obj:
            del data['id']
            serializer = UserSerializer(obj, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({
            'msg': '修改成功',
            'success': True
        }, status.HTTP_200_OK)

    # 删除用户
    def delete(self, request, *args, **kwargs):
        data = request.GET
        user_id = data.get('id')
        u = User.objects.get(id=user_id)
        u.delete()
        return Response({
            'msg': '删除用户成功',
            'success': True,
            'data': UserSerializer(u).data
        }, status.HTTP_200_OK)
