# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 9:51
# @Author  : NoWords
# @FileName: urls.py
from django.urls import path, re_path

from core.category.category_view import CategoryAPIView
from core.comment.comment_view import CommentAPIView
from core.config.config_view import ConfigAPIView
from core.deeds.deeds_view import DeedsAPIView
from core.discover.discover_view import DiscoverAPIView
from core.tags.tags_view import TagsAPIView
from core.site.site_view import SiteAPIView
from core.travel.travel_view import UserTravelAPIView
from core.user.user_view import UserAPIView
from core.video.base_video_view import BaseVideoAPIView
from core.upload.upload_view import FileUploadView, VideoUploadView
from django.views.static import serve
from aoi.settings import MEDIA_ROOT

urlpatterns = [
    path('api/v1/site', SiteAPIView.as_view()),
    path('api/v1/user', UserAPIView.as_view()),
    path('api/v1/tags', TagsAPIView.as_view()),
    path('api/v1/category', CategoryAPIView.as_view()),
    path('api/v1/config', ConfigAPIView.as_view()),
    path('api/v1/video', BaseVideoAPIView.as_view()),
    path('api/v1/comment', CommentAPIView.as_view()),
    path('api/v1/deeds', DeedsAPIView.as_view()),
    path('api/v1/discover', DiscoverAPIView.as_view()),
    path('api/v1/user/travel', UserTravelAPIView.as_view()),
    path('api/v1/upload/file', FileUploadView.as_view()),
    path('api/v1/upload/video', VideoUploadView.as_view()),
    re_path(r"^media/(?P<path>.*)", serve, {"document_root": MEDIA_ROOT}),
]
