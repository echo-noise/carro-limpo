from django.urls import path

from .views import PerfilView, SalvarImagemView

urlpatterns = [
    path('', PerfilView.as_view(), name="perfil"),
    path('salvar/imagem/<int:pk>', SalvarImagemView.as_view(),
         name="salvar_imagem"),
]
