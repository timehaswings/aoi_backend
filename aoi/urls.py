"""aoi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # 文档参考：https://jpadilla.github.io/django-rest-framework-jwt/
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/token/auth', obtain_jwt_token),
    url(r'^api/v1/token/refresh', refresh_jwt_token),
    url(r'^api/v1/token/verify', verify_jwt_token),
    url(r'^api/v1/captcha', include('rest_captcha.urls')),
    re_path(r'^', include('core.urls'))
]
