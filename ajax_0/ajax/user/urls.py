from django.conf.urls import url
from . import views

urlpatterns = [
    # 获取xhr对象
    url(r'^xhr$', views.xhr, name='xhr'),

    url(r'^get-xhr$', views.get_xhr, name='get_xhr'),
    url(r'^get-xhr-server', views.get_xhr_server, name='get_xhr_server'),
    # user register
    url(r'^register/$', views.register, name='register'),
    # user/checkuname/
    url(r'^checkuname/$', views.checkunme, name='checkuname'),
    # user/makepost/
    url(r'^make_post/$', views.make_post, name='make_post'),
    # user/get_user/
    url(r'^get_user/$', views.get_user, name='get_user'),
    # user/get_user/server/
    url(r'^get_user_server/$', views.get_user_server, name='get_user_server'),
    # user/json_obj
    url(r'^json_obj/$', views.json_obj, name='json_obj'),
    url(r'^json_dumps/$', views.json_dumps, name='json_dumps'),


]
