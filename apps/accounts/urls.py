from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from .views import *

urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("recovery/", PasswordResetView.as_view(), name='recovery'),
    path("recovery/reset/", PasswordResetView.as_view(), name="password_reset"),
    path("recovery/sent/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('recovery/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("recovery/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]