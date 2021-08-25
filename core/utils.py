# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 13:02
# @Author  : NoWords
# @FileName: utils.py
from core.serializers import UserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    """
    Returns the response data for both the login and refresh views.
    Override to return a custom response such as including the
    serialized representation of the User
    """
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
