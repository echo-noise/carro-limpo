from django.db import models
from django.db.models import Sum

from .models import Caixa, Transacao

INC = 'inc'
EXP = 'exp'


# managers
class CaixaManager(models.Manager):
    def get_current_user_instance(self, user):
        return Caixa.objects.filter(user=user, aberto=True).first()


class TransacaoManager(models.Manager):
    def get_by_caixa(self, caixa):
        return Transacao.objects.filter(caixa=caixa)

    def get_budget_querysets(self, caixa):
        _cache = self.get_by_caixa(caixa)
        return [_cache.filter(type=INC), _cache.filter(type=EXP)]

    def get_budget_dicts(self, queryset):
        dicts = []

        for transacao in queryset:
            dicts.append(transacao.get_dict())

        return dicts

    def get_current_totals(self, queryset):
        return queryset.aggregate(Sum('value')).get("value__sum", 0.00)

    def get_queryset_dict(self, queryset):
        dicts = []

        if queryset.exists():
            dicts.append(self.get_budget_dicts(queryset))
        else:
            dicts.append([])

        return dicts

