from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^add_book", views.add_view),
    url(r"^add_auth", views.auth_view),
    url(r"^list", views.list_view),
    url(r"^authlis", views.authlis_view),
    url(r"^mod/(\d+)", views.mod_view),  # 传输id参数
    url(r"^highly_mod/(\d+)", views.highly_mod_view),  # 传输id参数
    url(r"^del/(\d+)", views.del_view),  # 传输id参数
    url(r"^plist", views.plist_view),
    url(r"^clist", views.clist_view),
    url(r"^bar_list", views.bar_list_view),
    url(r"^xxxlist", views.xxxlist_view),

]
