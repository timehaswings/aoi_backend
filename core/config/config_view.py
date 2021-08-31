# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 15:06
# @Author  : NoWords
# @FileName: config_view.py
from core.models import Config
from core.serializers import ConfigSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class ConfigAPIView(APIView):
    """
    配置管理视图
    """

    def get(self, request, format=None):
        """
        查询数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        page_size = data.get('pageSize')
        page_no = data.get('pageNo')
        codename = data.get('codename')
        config_id = data.get('id')
        filters = {'is_delete': False}
        if config_id:
            filters['id'] = config_id
        if codename:
            filters['codename'] = codename
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = Config.objects.filter(**filters)[start:end]
        else:
            rows = Config.objects.filter(**filters)
        result = {
            'msg': '获取成功',
            'success': True,
            'data': {
                'rows': ConfigSerializer(rows, many=True).data,
                'total': rows.count()
            }
        }
        return Response(result, status.HTTP_200_OK)

    def post(self, request, format=None):
        """
        新增数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.data
        data['create_id'] = request.user.id
        data['updater_id'] = data['create_id']
        data['create_name'] = request.user.username
        data['updater_name'] = data['create_name']
        serializer = ConfigSerializer(data=data)
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
            'success': True,
        }, status.HTTP_200_OK)

    def put(self, request, format=None):
        """
        修改数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.data
        data['updater_id'] = request.user.id
        data['updater_name'] = request.user.username
        config_id = data.get('id')
        config = Config.objects.filter(id=config_id).first()
        if not config:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = ConfigSerializer(config, data=data, partial=True)
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
            'success': True,
        }, status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        删除数据视图
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        config_id = data.get('id')
        config = Config.objects.get(id=config_id)
        if not config:
            return Response({
                'msg': '数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        config.is_delete = True
        config.save()
        return Response({
            'msg': '删除成功',
            'success': ConfigSerializer(config).data
        }, status.HTTP_200_OK)
