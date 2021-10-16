from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    documento = models.CharField(max_length=20) 
    observacao = models.CharField(max_length=280)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    proprietario = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    placa = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {}".format(self.marca, self.modelo, self.placa)