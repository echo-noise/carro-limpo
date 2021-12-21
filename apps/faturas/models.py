from django.db import models
from django.contrib.auth.models import User
from datetime import date

from apps.clientes.models import Cliente
from apps.servicos.models import Servico

# Create your models here.
class Fatura(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cliente = models.OneToOneField(Cliente, on_delete=models.PROTECT)
    servico = models.OneToOneField(Servico, on_delete=models.PROTECT)
    data = models.DateField(default=date.today)
    gerado = models.BooleanField(default=False)