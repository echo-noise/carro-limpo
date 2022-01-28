from django.urls import path

from .views import (CaixaView, CaixaAbrirView, CaixaGetDataView,
                    CaixaFecharView, CaixaDeleteAllView, TransacaoFormView,
                    TransacaoDeleteView)

urlpatterns = [
    path("", CaixaView.as_view(), name="caixa"),
    path("abrir", CaixaAbrirView.as_view(), name="abrir_caixa"),
    path("get/", CaixaGetDataView.as_view(), name="get_caixa"),
    path("fechar/<int:pk>", CaixaFecharView.as_view(), name="fechar_caixa"),
    path("deleteall/", CaixaDeleteAllView.as_view(),
         name="deletar-transacoes"),
    path("insert/", TransacaoFormView.as_view(), name="salvar"),
    path("delete/<int:pk>", TransacaoDeleteView.as_view(), name="excluir")
]
