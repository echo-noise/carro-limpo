from django.urls import path

from .views import *

urlpatterns = [
    path('', perfil, name="perfil"),
    path('salvar/', salvar_perfil, name="salvar_perfil"),
    path('salvar/imagem/', salvar_imagem, name="salvar_imagem"),
    path('salvar/estabelecimento/', salvar_estabelecimento, name="salvar_estabelecimento")
]