"""mys2 URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sum/', views.sum_view),
    # 模拟get和post请求
    url(r'^login', views.login_view),
    url(r'^login2', views.login2_view),

    # 模拟后端向前端传参
    url(r'^test2', views.test2_view),
    url(r'^connectdb', views.connectdb_view),


    # 模拟前后端数据交互
    # url(r'^mycal', views.mycal_view),
]
