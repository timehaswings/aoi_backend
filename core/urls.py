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
from core.area.area_view import AreaAPIView
from core.travel.travel_view import UserTravelAPIView
from core.user.user_view import UserAPIView, PasswordAPIView
from core.user.group_view import GroupAPIView
from core.user.permission_view import PermissionAPIView
from core.home import category_view, menu_view, config_view, index_view, recommend_view
from core.user.group_perm_view import GroupPermAPIView
from core.user.user_group_view import UserGroupAPIView
from core.user.group_menu_view import GroupMenuAPIView, UserMenuAPIView
from core.video.base_video_view import BaseVideoAPIView
from core.menu.menu_view import MenuAPIView
from core.upload.upload_view import FileUploadView, VideoUploadView
from .views import RegisterAPIView
from django.views.static import serve
from aoi.settings import MEDIA_ROOT

urlpatterns = [
    path('api/v1/register', RegisterAPIView.as_view()),
    path('api/v1/home/config', config_view.ConfigApiView.as_view()),
    path('api/v1/home/category', category_view.CategoryApiView.as_view()),
    path('api/v1/home/tags', category_view.TagsApiView.as_view()),
    path('api/v1/home/area', category_view.AreaApiView.as_view()),
    path('api/v1/home/video', category_view.VideoApiView.as_view()),
    path('api/v1/home/index/carousel', index_view.CarouselApiView.as_view()),
    path('api/v1/home/index/category', index_view.CategoryVideoApiView.as_view()),
    path('api/v1/home/public/menu', menu_view.PublicMenuApiView.as_view()),
    path('api/v1/home/private/menu', menu_view.PrivateMenuApiView.as_view()),
    path('api/v1/home/video/recommend', recommend_view.RecommendApiView.as_view()),
    path('api/v1/site', SiteAPIView.as_view()),
    path('api/v1/user', UserAPIView.as_view()),
    path('api/v1/password', UserAPIView.as_view()),
    path('api/v1/group', GroupAPIView.as_view()),
    path('api/v1/permission', PasswordAPIView.as_view()),
    path('api/v1/group/permission', GroupPermAPIView.as_view()),
    path('api/v1/user/menu', UserMenuAPIView.as_view()),
    path('api/v1/group/menu', GroupMenuAPIView.as_view()),
    path('api/v1/user/group', UserGroupAPIView.as_view()),
    path('api/v1/tags', TagsAPIView.as_view()),
    path('api/v1/area', AreaAPIView.as_view()),
    path('api/v1/category', CategoryAPIView.as_view()),
    path('api/v1/config', ConfigAPIView.as_view()),
    path('api/v1/video', BaseVideoAPIView.as_view()),
    path('api/v1/comment', CommentAPIView.as_view()),
    path('api/v1/deeds', DeedsAPIView.as_view()),
    path('api/v1/discover', DiscoverAPIView.as_view()),
    path('api/v1/menu', MenuAPIView.as_view()),
    path('api/v1/user/travel', UserTravelAPIView.as_view()),
    path('api/v1/upload/file', FileUploadView.as_view()),
    path('api/v1/upload/video', VideoUploadView.as_view()),
    re_path(r"^media/(?P<path>.*)", serve, {"document_root": MEDIA_ROOT}),
]
