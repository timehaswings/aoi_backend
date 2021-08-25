# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 9:51
# @Author  : NoWords
# @FileName: urls.py
from django.urls import path, re_path

from .site.site_view import SiteAPIView
from .user.user_view import UserAPIView
from .upload.upload_view import FileUploadView, VideoUploadView
from django.views.static import serve
from aoi.settings import MEDIA_ROOT

urlpatterns = [
    path('api/v1/site', SiteAPIView.as_view()),
    path('api/v1/user', UserAPIView.as_view()),
    path('api/v1/upload/file', FileUploadView.as_view()),
    path('api/v1/upload/video', VideoUploadView.as_view()),
    re_path(r"^media/(?P<path>.*)", serve, {"document_root": MEDIA_ROOT}),
]
