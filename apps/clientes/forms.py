from django import forms

from .models import Cliente
from carro_limpo.forms import UserRequiredForm

class ClienteCreateForm(UserRequiredForm):
    class Meta:
        model = Cliente
        exclude = ('user',)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ('user',)