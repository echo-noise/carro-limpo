import django.forms as forms
from django.contrib.auth.hashers import check_password
from .models import Endereco, Perfil, Loja

class UserProfileForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Nome")
    user_fone = forms.CharField(max_length=15, label="Telefone")
    user_email = forms.EmailField(max_length=100, label="E-mail")
    password = forms.CharField(max_length=20, label="Senha")
    new_password = forms.CharField(max_length=20, required=False)
    confirm_password = forms.CharField(max_length=20, required=False)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(UserProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        _password = cleaned_data.get("password")

        if not check_password(_password, self.request.user.password):
            self.add_error('password', forms.ValidationError('Senha incorreta'))

        _new_password = cleaned_data.get("new_password")
        _confirm_password = cleaned_data.get("confirm_password")

        if _new_password != _confirm_password:
            self.add_error('new_password', forms.ValidationError('Senhas não coincidem'))

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