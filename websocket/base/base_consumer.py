# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/30 9:06
# @Author  : NoWords
# @FileName: base_consumer.py
import json
from channels.generic.websocket import WebsocketConsumer


class BaseConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print('connect')

    def disconnect(self, close_code):
        print('disconnect')

    def receive(self, text_data):
        print(text_data)