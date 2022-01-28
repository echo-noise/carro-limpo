from django.urls import path

from .views import (FaturaListarView, FaturaFormView, FaturaDeleteView,
                    FaturaUpdateView, gerar)

urlpatterns = [
    path("", FaturaListarView.as_view(), name="faturas"),
    path("salvar/", FaturaFormView.as_view(), name="salvar"),
    path("gerar/<int:id>", gerar, name="gerar"),
    path("delete/<int:pk>", FaturaDeleteView.as_view(), name="delete"),
    path("edit/<int:pk>", FaturaUpdateView.as_view(), name="edit"),

]
