from django.urls import path

from .views import *

urlpatterns = [
    path("", ClienteListView.as_view(), name="clientes"),
    path("insert", inserir, name="inserir"),
    path("excluir/<int:id>", excluir, name="excluir"),
]