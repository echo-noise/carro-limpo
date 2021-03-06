from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum
from django.utils.timezone import now

from apps.caixa.models import Caixa


class EstatisticasView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(EstatisticasView, self).get_context_data(**kwargs)
        hoje = now()

        _cache = Caixa.objects.filter(user=self.request.user) \
                      .filter(data__year=hoje.year) \
                      .filter(data__month=hoje.month)

        receita = _cache.aggregate(Sum('receita')).get("receita__sum", 0.00)
        despesa = _cache.aggregate(Sum('despesa')).get("despesa__sum", 0.00)
        servicos = _cache.aggregate(Sum('servicos')).get("servicos__sum", 0)
        clientes = _cache.aggregate(Sum('clientes')).get("clientes__sum", 0)

        if receita:
            context['receita'] = receita
        else:
            context['receita'] = 0

        if despesa:
            context['despesa'] = despesa
        else:
            context['despesa'] = 0

        if servicos:
            context['servicos'] = servicos
        else:
            context['servicos'] = 0

        if clientes:
            context['clientes'] = clientes
        else:
            context['clientes'] = 0

        return context
