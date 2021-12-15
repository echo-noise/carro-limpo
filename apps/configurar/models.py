from django.db import models

# Create your models here.
class Estabelecimento(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=50)
    telefone = models.CharField(max_length = 15)
    email = models.EmailField(max_length=100)
    cep = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)