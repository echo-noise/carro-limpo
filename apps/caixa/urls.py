from django.urls import path

from .views import * 

urlpatterns = [
    path("", caixa, name="caixa"),
    path("abrir", abrir_caixa, name="abrir_caixa"),
    path("get/", CaixaGetDataView.as_view(), name="get_caixa"),
    path("insert/", TransacaoFormView.as_view(), name="salvar"),
    path("delete/<int:pk>", TransacaoDeleteView.as_view(), name="excluir")
]