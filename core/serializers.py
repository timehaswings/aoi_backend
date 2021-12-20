# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 9:56
# @Author  : NoWords
# @FileName: serializers.py
from django.contrib.auth.models import User, Group, Permission
from django.contrib.sites.models import Site
from rest_framework.validators import UniqueValidator
from aoi.settings import BASE_VIDEO_URL, BASE_THUMB_URL

from core.models import Tags, Category, BaseVideo, \
    Comment, Config, UserTravel, Deeds, Discover
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['date_joined']


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        allow_blank=False,
        trim_whitespace=True,
        validators=[UniqueValidator(queryset=Tags.objects.all())])
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_name = serializers.CharField(max_length=40)
    updater_name = serializers.CharField(max_length=40)

    class Meta:
        model = Tags
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        allow_blank=False,
        trim_whitespace=True,
        validators=[UniqueValidator(queryset=Tags.objects.all())])
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_name = serializers.CharField(max_length=40)
    updater_name = serializers.CharField(max_length=40)

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class BaseVideoSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=200,
        allow_blank=False,
        trim_whitespace=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    release_time = serializers.DateField(format='%Y-%m-%d')
    m3u8 = serializers.SerializerMethodField(read_only=True)
    thumb = serializers.SerializerMethodField(read_only=True)
    category_obj = CategorySerializer(source="category", read_only=True)
    tags_list = TagsSerializer(source="tags", read_only=True, many=True)
    create_name = serializers.CharField(max_length=40)
    updater_name = serializers.CharField(max_length=40)

    def get_m3u8(self, obj):
        return '%s%s/index.m3u8' % (BASE_VIDEO_URL, obj.m3u8_path)

    def get_thumb(self, obj):
        return '%s%s/thumb-500.jpg' % (BASE_THUMB_URL, obj.thumb_path)

    class Meta:
        model = BaseVideo
        fields = '__all__'
        extra_kwargs = {
            'is_delete': {'write_only': True},
            'm3u8_path': {'write_only': True},
            'thumb_path': {'write_only': True},
            'category': {'write_only': True},
            'tags': {'write_only': True},
        }
        read_only_fields = ['create_time']


class DiscoverSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=50,
        allow_blank=False,
        trim_whitespace=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_name = serializers.CharField(max_length=40)
    updater_name = serializers.CharField(max_length=40)

    class Meta:
        model = Discover
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class CommentSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_name = serializers.CharField(max_length=40)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class ConfigSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=80,
        allow_blank=False,
        trim_whitespace=True)
    codename = serializers.CharField(
        max_length=40,
        allow_blank=False,
        trim_whitespace=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_name = serializers.CharField(max_length=40)
    updater_name = serializers.CharField(max_length=40)

    class Meta:
        model = Config
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class UserTravelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    video_obj = BaseVideoSerializer(source="video", read_only=True)
    discover_obj = DiscoverSerializer(source="discover", read_only=True)

    class Meta:
        model = UserTravel
        fields = '__all__'
        extra_kwargs = {
            'is_delete': {'write_only': True},
            'video': {'write_only': True},
            'discover': {'write_only': True}
        }
        read_only_fields = ['create_time']


class DeedsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        max_length=80,
        allow_blank=False,
        trim_whitespace=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    create_name = serializers.CharField(max_length=40)
    updater_name = serializers.CharField(max_length=40)

    class Meta:
        model = Deeds
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
