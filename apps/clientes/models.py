from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, default=None)
    telefone = models.CharField(max_length=15, default=None)
    email = models.EmailField(max_length=100, default = None)
    documento = models.CharField(max_length=20, default=None) 
    placa = models.CharField(max_length=50, default=None)
    marca = models.CharField(max_length=100, default=None)
    modelo = models.CharField(max_length=100, default=None)
    cor = models.CharField(max_length=100, default=None)

    def __str__(self):
        return "{nome} ({placa})".format(nome=self.nome, placa=self.placa)