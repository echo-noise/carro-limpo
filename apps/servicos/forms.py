from carro_limpo.forms import UserRequiredForm
from .models import Servico


class ServicoCreateForm(UserRequiredForm):
    class Meta:
        model = Servico
        exclude = ('user',)
