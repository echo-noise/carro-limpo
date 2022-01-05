from django.urls import path

from .views import *

urlpatterns = [
    path("", listar, name="faturas"),
    path("salvar/", salvar, name="salvar"),
    path("gerar/<int:id>", gerar, name="gerar"),
    path("delete/<int:id>", excluir, name="delete"),
    path("edit/<int:id>", atualizar, name="edit"),

]