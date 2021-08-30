# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/28 10:56
# @Author  : NoWords
# @FileName: asgi.py
import os

from asgiref.wsgi import WsgiToAsgi
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from channels.auth import AuthMiddlewareStack
import websocket.urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aoi.settings")

# django_asgi_app = get_asgi_application()
django_asgi_app = WsgiToAsgi(get_wsgi_application())

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket.urls.urlpatterns
        )
    )
})
