from django.urls import path

from .views import *

urlpatterns = [
    path("", ClienteListarView.as_view(), name="clientes"),
    path("insert", ClienteCreateView.as_view(), name="inserir"),
    path("delete/<int:pk>", ClienteDeleteView.as_view(), name="excluir"),
    path("update/<int:pk>", ClienteUpdateView.as_view(), name="atualizar"),
]