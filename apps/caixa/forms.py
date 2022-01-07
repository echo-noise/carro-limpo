from django import forms

from .models import Transacao

class TransacaoBaseForm(forms.ModelForm):

    class Meta:
        model = Transacao
        fields = ('value',)

    def save(self, caixa, commit=True):
        _obj = super(TransacaoBaseForm, self).save(commit=False)
        _obj.caixa = caixa

        if commit:
            _obj.save()

        return _obj

class TransacaoForm(TransacaoBaseForm):
    class Meta(TransacaoBaseForm.Meta):
        fields = TransacaoBaseForm.Meta.fields + ('description', 'type')