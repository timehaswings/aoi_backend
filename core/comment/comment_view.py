# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 11:38
# @Author  : NoWords
# @FileName: comment_view.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers

from ..serializers import CommentSerializer
from ..models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CommentAPIView(APIView):
    """
    分类管理
    """

    @method_decorator(cache_page(60))
    @method_decorator(vary_on_headers("Authorization", ))
    def get(self, request, *args, **kwargs):
        """
        获取分类列表
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        comment_id = data.get('id')
        content = data.get('content')
        filters = {'is_delete': 0}
        if comment_id:
            filters['id'] = comment_id
        if content:
            filters['content__contains'] = content
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Comment.objects.filter(**filters)[start:end]
        else:
            rows = Comment.objects.filter(**filters)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': CommentSerializer(rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        新增数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        serializer = CommentSerializer(data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '添加失败：%s' % e,
                'success': False
            }, status.HTTP_200_OK)
        return Response({
            'msg': '添加成功',
            'success': True
        }, status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        修改数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        comment_id = data.get('id')
        comment = Comment.objects.filter(id=comment_id).first()
        if not comment:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = CommentSerializer(comment, data=data, partial=True)
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
        删除数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.GET
        comment_id = data.get('id')
        comment = Comment.objects.get(id=comment_id)
        if not comment:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        comment.delete()
        return Response({
            'msg': '删除用户成功',
            'success': True,
            'data': CommentSerializer(comment).data
        }, status.HTTP_200_OK)

