from django.urls import path

from .views import ListarVeiculoView, excluir

urlpatterns = [
    path("", ListarVeiculoView.as_view(), name="clientes"),
    path("excluir/<int:id>", excluir, name="excluir"),
]