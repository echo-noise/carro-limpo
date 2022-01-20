from django import forms
from django.contrib.auth.hashers import check_password
from .models import Endereco, Perfil, Loja
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'email']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['telefone',]

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        exclude = ('user', )

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        exclude = ('user',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('imagem', )