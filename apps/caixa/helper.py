from django.db.models import Sum

from .models import Caixa, Transacao

INC = 'inc'
EXP = 'exp'


def buscar_caixa_atual(user):
    return Caixa.objects.filter(user=user, aberto=True).first()


def transacao_get_total(queryset):
    return queryset.aggregate(Sum('value')).get("value__sum", 0.00)


def transacao_make_dict(queryset):
    transacoes = []

    for transacao in queryset:
        transacoes.append({"id": int(transacao.id),
                           "value": float(transacao.value),
                           "description": transacao.description})

    return transacoes


def get_querysets(caixa):
    _cache = Transacao.objects.filter(caixa=caixa)
    return [_cache.filter(type=INC), _cache.filter(type=EXP)]


def caixa_as_dict(caixa):
    inc = []
    exp = []
    inc_total = 0
    exp_total = 0
    percentage = 0
    budget = 0

    if caixa:
        querysets = get_querysets(caixa)

        if querysets[0].exists():
            inc = transacao_make_dict(querysets[0])
            inc_total = transacao_get_total(querysets[0])
        if querysets[1].exists():
            exp = transacao_make_dict(querysets[1])
            exp_total = transacao_get_total(querysets[1])

        if inc_total and exp_total:
            percentage = round((exp_total / inc_total) * 100)

        budget = inc_total - exp_total

    data = {
        "allItems": {"exp": exp, "inc": inc},
        "totals": {"exp": float(exp_total), "inc": float(inc_total)},
        "budget": float(budget),
        "percentage": percentage
    }

    return data
