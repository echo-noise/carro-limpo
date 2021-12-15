from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField(max_length=50, default=None)
    valor = models.DecimalField(decimal_places=2, max_digits=14)

    def __str__(self):
        return self.nome