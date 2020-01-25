from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^add_book", views.add_view),
    url(r"^add_auth",views.auth_view),

]
