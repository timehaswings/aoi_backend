# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 9:56
# @Author  : NoWords
# @FileName: serializers.py
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from core.models import Tags, Category, BaseVideo, \
    Comment, Config, UserTravel, Deeds, Discover
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    username = serializers.EmailField()

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['date_joined']


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Tags
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time', 'update_time']


class CategorySerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time', 'update_time']


class BaseVideoSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    release_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = BaseVideo
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time', 'update_time']


class CommentSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']


class ConfigSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Config
        fields = '__all__'
        read_only_fields = ['create_time']


class UserTravelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = UserTravel
        fields = '__all__'
        read_only_fields = ['create_time']


class DeedsSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Deeds
        fields = '__all__'
        read_only_fields = ['create_time']


class DiscoverSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Discover
        fields = '__all__'
        extra_kwargs = {'is_delete': {'write_only': True}}
        read_only_fields = ['create_time']
