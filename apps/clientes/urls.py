from django.urls import path

from .views import *

urlpatterns = [
    path("list", listar, name="clientes"),
    path("insert", inserir, name="inserir"),
    path("delete/<int:id>", excluir, name="excluir"),
    path("update/<int:id>", atualizar, name="atualizar"),
]