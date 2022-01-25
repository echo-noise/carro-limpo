
from django.urls import path

from .views import *

urlpatterns = [
    path("", EstatisticasView.as_view(), name="home"),
]