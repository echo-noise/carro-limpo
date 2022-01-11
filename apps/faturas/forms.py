from django import forms

from .models import Fatura

class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        exclude = ('user', 'data', 'pago')
    
    def save(self, user, commit=True):
        _obj = super(FaturaForm, self).save(commit=False)
        _obj.user = user

        if commit:
            _obj.save()

        return _obj
