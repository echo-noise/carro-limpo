
from django.urls import path

from .views import EstatisticasView

urlpatterns = [
    path("", EstatisticasView.as_view(), name="home"),
]
