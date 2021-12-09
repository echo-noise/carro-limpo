from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path("login/", login_page, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]