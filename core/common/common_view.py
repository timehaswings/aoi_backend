# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/20 10:04
# @Author  : NoWords
# @FileName: common_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)


class CommonAPIView(APIView):
    """
    基础视图
    """

    model_name = None
    serializer_name = None
    filters = {'is_delete': 0}
    page_size_field = 'pageSize'
    page_no_field = 'pageNo'
    # eg: [{'filter_key': 'name__contains', 'request_key': 'name'}]
    query = None
    sort_list = ['-id']
    # eg: {'db_field': 'value'}
    add_extra_data = None
    # eg: {'db_field': 'value'}
    update_extra_data = None

    def check_model(self):
        """
        模型检查
        :return:
        """
        if not self.model_name:
            return Response({
                'msg': '该视图未配置模型',
                'success': False
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def check_serializer(self):
        """
        序列化器检查
        :return:
        """
        if not self.serializer_name:
            return Response({
                'msg': '该视图未配置序列化器',
                'success': False
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def set_add_extra_data(self, data):
        self.add_extra_data = data

    def set_update_extra_data(self, data):
        self.update_extra_data = data

    def get(self, request, *args, **kwargs):
        """
        获取列表数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.check_model()
        data = request.GET
        page_size, page_no = None, None
        if self.page_size_field and self.page_no_field:
            page_size = data.get(self.page_size_field)
            page_no = data.get(self.page_no_field)
        if self.filters:
            filters = self.filters.copy()
        else:
            filters = {}
        if self.query:
            for param in self.query:
                if data.get(param['request_key']):
                    filters[param['filter_key']] = data.get(param['request_key'])
        if self.sort_list:
            sort_list = self.sort_list
        else:
            sort_list = []
        if page_size and page_no:
            start = (int(page_no) - 1) * int(page_size)
            end = start + int(page_size)
            rows = globals()[self.model_name].objects.filter(**filters).order_by(*sort_list)[start:end]
        else:
            rows = globals()[self.model_name].objects.filter(**filters).order_by(*sort_list)
        return Response({
            'msg': '获取成功',
            'success': True,
            'data': {'rows': globals()[self.serializer_name](rows, many=True).data, 'total': rows.count()}
        }, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        新增数据
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.check_serializer()
        data = request.data
        if self.add_extra_data:
            data = {**data, **self.add_extra_data}
        serializer = globals()[self.serializer_name](data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '添加数据失败：%s' % e,
                'success': False
            }, status.HTTP_200_OK)
        return Response({
            'msg': '添加数据成功',
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
        self.check_serializer()
        data = request.data
        if self.update_extra_data:
            data = {**data, **self.update_extra_data}
        data_id = data.get('id')
        if not data_id:
            return Response({
                'msg': '数据id缺失',
                'success': False
            }, status.HTTP_200_OK)
        row = globals()[self.model_name].objects.filter(id=data_id).first()
        if not row:
            return Response({
                'msg': '修改失败，数据不存在',
                'success': False
            }, status.HTTP_200_OK)
        serializer = globals()[self.serializer_name](row, data=data, partial=True)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'msg': '修改成功',
                'success': True
            }, status.HTTP_200_OK)
        except Exception as e:
            logger.error('error: %s' % e)
            return Response({
                'msg': '修改失败：%s' % e,
                'success': False
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
        data_id = data.get('id')
        if not data_id:
            return Response({
                'msg': '数据id缺失',
                'success': False
            }, status.HTTP_200_OK)
        if 'is_delete' in self.filters:
            globals()[self.model_name].objects.filter(id=data_id).update(is_delete=True)
        else:
            globals()[self.model_name].objects.filter(id=data_id).delete()
        return Response({
            'msg': '删除数据成功',
            'success': True,
        }, status.HTTP_200_OK)
