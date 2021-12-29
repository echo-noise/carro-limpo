from django.db import models
from django.contrib.auth.models import User
from datetime import date

from apps.clientes.models import Cliente
from apps.servicos.models import Servico
from apps.caixa.models import Transacao

# Create your models here.
class Fatura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transacao = models.OneToOneField(Transacao, on_delete=models.CASCADE, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField(default=date.today)
    pago = models.BooleanField(default=False)