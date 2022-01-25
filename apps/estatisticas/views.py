from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum 
from django.utils.timezone import now


from apps.caixa.models import Caixa
from apps.clientes.models import Cliente

class EstatisticasView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(EstatisticasView, self).get_context_data(**kwargs)
        hoje = now()

        # filtrar por usuario
        _cache = Caixa.objects.filter(user=self.request.user)
        # filtrar por ano
        _cache = _cache.filter(data__year=hoje.year)
        # filtrar por mes
        _cache = _cache.filter(data__month=hoje.month)

        receita = _cache.aggregate(Sum('receita')).get("value__sum", 0.00)
        despesa = _cache.aggregate(Sum('despesa')).get("value__sum", 0.00)
        servicos = _cache.aggregate(Sum('servicos')).get("value__sum", 0)
        clientes = _cache.aggregate(Sum('clientes')).get("value__sum", 0)

        context['receita'] = receita
        context['despesa'] = despesa
        context['servicos'] = servicos
        context['clientes'] = clientes
        print(context)
        return context