# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/2 11:52
# @Author  : NoWords
# @FileName: validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    """
    偶数验证器
    :param value:
    :return:
    """
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
