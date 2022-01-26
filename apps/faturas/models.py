from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _

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
    data = models.DateField(auto_now=True)
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
        return False
    
    def clean(self):
        super().clean()

        if self.pago:
            transacao = self.criar_transacao()
            if not transacao:
                raise ValidationError(_('Não foi possível alterar o status pois não foi possivel criar uma transação associada à fatura. Note que é necessário ter um caixa aberto para criar a transação.'))
        else:
            if self.transacao:
                self.transacao.delete()
                self.transacao = None

    @receiver(pre_save)
    def pre_save_handler(sender, instance, *args, **kwargs):
        instance.full_clean()
