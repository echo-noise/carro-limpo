from django.db import models
from django.contrib.auth.models import User
from datetime import date

from apps.faturas.models import Fatura

# Create your models here.
class Caixa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.DateField(default=date.today, unique=True)
    aberto = models.BooleanField(default=False)

class Transacao(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
    fatura = models.ForeignKey(Fatura, on_delete=models.CASCADE, blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=100)
