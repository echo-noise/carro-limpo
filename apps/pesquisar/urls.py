from django.urls import path

from .views import SearchAllView

urlpatterns = [path("", SearchAllView.as_view(), name="search_all")]
