from django.urls import path

from .views import *

urlpatterns = [
    path("", ServicoListarView.as_view(), name="servicos"),
    path("insert", ServicoCreateView.as_view(), name="inserir"),
    path("delete/<int:pk>", ServicoDeleteView.as_view(), name="excluir"),
    path("update/<int:pk>", ServicoUpdateView.as_view(), name="atualizar"),
]