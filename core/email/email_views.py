# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/12/16 9:16
# @Author  : NoWords
# @FileName: email_views.py

import logging
from smtplib import SMTPException

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from aoi.settings import EMAIL_HOST_USER

logger = logging.getLogger(__name__)


def send_notice(subject, message, user_id):
    """
    发送普通邮件
    :param subject: 主题
    :param message: 内容
    :param user_id: 收件人
    :return: 是否发送成功
    """
    receiver = User.objects.get(id=user_id).email
    if not receiver:
        return False
    try:
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            [receiver],
            fail_silently=False,
        )
        return True
    except SMTPException as e:
        logger.error('%s' % e)
        return False


def send_beauty_notice(subject, message, user_id):
    """
    发送美化的邮件
    :param subject: 主题
    :param message: 消息
    :param user_id: 收件人
    :return: 邮件是否发送成功
    """
    user = User.objects.get(id=user_id)
    if not user:
        return False
    text_content = render_to_string('email.txt', {'account': user.name, 'message': message})
    html_content = render_to_string('email.html', {'account': user.name, 'message': message})
    try:
        msg = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except SMTPException as e:
        logger.error(e)
        return False
