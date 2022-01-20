from django.urls import path

from .views import *

urlpatterns = [
    path('', PerfilView.as_view(), name="perfil"),
    path('salvar/imagem/', salvar_imagem, name="salvar_imagem"),
]