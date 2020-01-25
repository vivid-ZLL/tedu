"""mysite3 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls import include

# 此处演示主路由分发地址给子路由
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^shebao', views.shebao_view),
    url(r'^music/', include("music.urls")),  # 此处传递的参数是字符串
    url(r'^index/', include("index.urls")),
    url(r'^sport/', include("sport.urls")),
    url(r'^news/', include("news.urls")),
    url(r'^bookstore/', include("bookstore.urls")),


]