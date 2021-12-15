from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50, default=None)
    telefone = models.CharField(max_length=15, default=None)
    email = models.EmailField(max_length=100, default = None)
    documento = models.CharField(max_length=20, default=None) 
    placa = models.CharField(max_length=50, default=None)
    marca = models.CharField(max_length=100, default=None)
    modelo = models.CharField(max_length=100, default=None)
    cor = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.nome