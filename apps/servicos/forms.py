from django import forms

from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        exclude = ('user',)