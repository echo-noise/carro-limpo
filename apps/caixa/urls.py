from django.urls import path

from .views import *

urlpatterns = [
    path("", caixa, name="caixa"),
    path("abrir", abrir_caixa, name="abrir_caixa"),
    path("get/", get_caixa, name="get_caixa"),
]