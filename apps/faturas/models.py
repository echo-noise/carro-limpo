from django.db import models
from django.contrib.auth.models import User
from datetime import date

from apps.clientes.models import Cliente
from apps.servicos.models import Servico
from apps.caixa.models import Transacao
from apps.caixa.helper import buscar_caixa_atual, INC

# Create your models here.
class Fatura(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transacao = models.OneToOneField(Transacao, on_delete=models.SET_NULL, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField(default=date.today)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return "Fatura: {servico} para {cliente} em {data}".format(servico=self.servico, cliente=self.cliente, data=self.data.strftime("%d/%m/%y"))
    
    def criar_transacao(self):
        _caixa = buscar_caixa_atual(self.user)

        if _caixa:
            self.transacao = Transacao(
                caixa = _caixa,
                type = INC,
                value = self.servico.valor,
                description = self.__str__()
            )
            self.transacao.save()
            return True


    def save(self, *args, **kwargs):
        if getattr(self, 'pago_changed', True):
            if self.pago:
                if self.criar_transacao():
                    super(Fatura, self).save(*args, **kwargs)
            else:
                if self.transacao:
                    self.transacao.delete()
                    self.transacao = None
                super(Fatura, self).save(*args, **kwargs)
