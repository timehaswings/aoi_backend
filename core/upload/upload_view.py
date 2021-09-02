# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 14:07
# @Author  : NoWords
# @FileName: upload_view.py
from rest_framework.parsers import MultiPartParser
from aoi.settings import VIDEO_STORAGE_PATH, MEDIA_ROOT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
import uuid
import os
import logging

logger = logging.getLogger(__name__)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        """
        可接受上传任何文件
        :param request:
        :param format:
        :return:
        """
        files = request.FILES.getlist("attachment", None)
        if not files or len(files) == 0:
            return Response({
                'msg': 'attachment参数缺失',
                'success': False
            }, status.HTTP_200_OK)
        files_address = []
        sub_dir = datetime.datetime.now().strftime("%Y%m%d")
        file_dir = os.path.join(MEDIA_ROOT, 'attachments', sub_dir)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        for file in files:
            new_name = str(uuid.uuid4()) + os.path.splitext(file.name)[1]
            file_absolute_path = os.path.join(file_dir, new_name)
            file_handler = open(file_absolute_path, 'wb')
            try:
                for chunk in file.chunks():
                    file_handler.write(chunk)
                files_address.append('attachments/' + sub_dir + '/' + new_name)
            finally:
                file_handler.close()
        return Response({
            'msg': '上传成功',
            'success': True,
            'data': files_address
        }, status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        移除指定文件
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        file_path = data.get('path')
        if not file_path:
            return Response({
                'msg': '文件路径缺失',
                'success': False
            }, status.HTTP_200_OK)
        file_absolute_path = os.path.join(MEDIA_ROOT, file_path)
        if os.path.exists(file_absolute_path):
            os.remove(file_absolute_path)
        return Response({
            'msg': '文件删除成功',
            'success': True
        }, status.HTTP_200_OK)


class VideoUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        """
        上传视频
        :param request:
        :param format:
        :return:
        """
        files = request.FILES.getlist("video", None)
        if not files or len(files) == 0:
            return Response({
                'msg': 'video参数缺失',
                'success': False
            }, status.HTTP_200_OK)
        files_address = []
        sub_dir = datetime.datetime.now().strftime("%Y%m%d")
        file_dir = os.path.join(VIDEO_STORAGE_PATH, sub_dir)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        for file in files:
            new_name = str(uuid.uuid4()) + os.path.splitext(file.name)[1]
            file_absolute_path = os.path.join(file_dir, new_name)
            file_handler = open(file_absolute_path, 'wb')
            try:
                for chunk in file.chunks():
                    file_handler.write(chunk)
                files_address.append(sub_dir + '/' + new_name)
            finally:
                file_handler.close()
        return Response({
            'msg': '上传成功',
            'success': True,
            'data': files_address
        }, status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        移除指定文件
        :param request:
        :param format:
        :return:
        """
        data = request.GET
        video_path = data.get('path')
        if not video_path:
            return Response({
                'msg': '视频路径缺失',
                'success': False
            }, status.HTTP_200_OK)
        video_absolute_path = os.path.join(VIDEO_STORAGE_PATH, video_path)
        if os.path.exists(video_absolute_path):
            os.remove(video_absolute_path)
        return Response({
            'msg': '视频删除成功',
            'success': True
        }, status.HTTP_200_OK)
