from django import forms

from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ('value', 'description', 'type')

    def save(self, caixa, commit=True):
        _obj = super(TransacaoForm, self).save(commit=False)
        _obj.caixa = caixa

        if commit:
            _obj.save()

        return _obj

class CaixaFecharForm(forms.Form):
    saldo_fisico = forms.DecimalField(max_digits=10, decimal_places=2)