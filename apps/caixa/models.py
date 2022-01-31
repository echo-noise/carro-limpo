from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Caixa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True, unique=True)
    receita = models.DecimalField(max_digits=12, decimal_places=2, blank=True,
                                  default=0)
    despesa = models.DecimalField(max_digits=12, decimal_places=2, blank=True,
                                  default=0)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, blank=True,
                                default=0)
    diferenca = models.DecimalField(max_digits=12, decimal_places=2,
                                    blank=True, default=0)
    clientes = models.IntegerField(blank=True, default=0)
    servicos = models.IntegerField(blank=True, default=0)
    aberto = models.BooleanField(default=True)


class Transacao(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=models.CASCADE)
    type = models.CharField(max_length=3)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=100, blank=True)

    def get_dict(self):
        return {
            "id": int(self.id),
            "value": float(self.value),
            "description": self.description
            }
