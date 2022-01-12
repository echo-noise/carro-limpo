from django import forms

class UserRequiredForm(forms.ModelForm):
    def save(self, user, commit=True):
        _obj = super(UserRequiredForm, self).save(commit=False)
        _obj.user = user

        if commit:
            _obj.save()

        return _obj
