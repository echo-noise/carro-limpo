from .models import Fatura
from carro_limpo.forms import UserRequiredForm


class FaturaForm(UserRequiredForm):
    class Meta:
        model = Fatura
        exclude = ('user', 'data', 'pago')
