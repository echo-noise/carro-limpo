from django import forms

from carro_limpo.forms import UserRequiredForm
from .models import Servico

class ServicoCreateForm(UserRequiredForm):
    class Meta:
        model = Servico
        exclude = ('user',)

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        exclude = ('user',)