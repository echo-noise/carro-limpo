from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Caixa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.DateField(default=date.today)
    aberto = models.BooleanField(default=False)
