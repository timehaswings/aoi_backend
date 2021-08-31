# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/26 11:38
# @Author  : NoWords
# @FileName: comment_view.py
from ..serializers import CommentSerializer
from ..models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CommentAPIView(APIView):
    """
    评论管理
    """

    def get(self, request, *args, **kwargs):
        """
        获取评论列表
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
        filters = {'is_delete': False}
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
        data['create_id'] = request.user.id
        data['create_name'] = request.user.username
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
        comment.is_delete = True
        comment.save()
        return Response({
            'msg': '删除评论成功',
            'success': True,
            'data': CommentSerializer(comment).data
        }, status.HTTP_200_OK)

