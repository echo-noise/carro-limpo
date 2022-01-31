from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, View, TemplateView, DeleteView

from apps.faturas.models import Fatura
from carro_limpo.helper import error_response, ADD

from .models import Caixa, Transacao
from .forms import TransacaoForm, CaixaFecharForm
from .helper import buscar_caixa_atual, caixa_as_dict


# caixa
class CaixaView(LoginRequiredMixin, TemplateView):
    template_name = "caixa.html"

    def get_context_data(self, **kwargs):
        context = super(CaixaView, self).get_context_data(**kwargs)
        _cache = Caixa.objects.filter(user=self.request.user)
        context['fluxo_caixa'] = _cache.filter(aberto=False)
        context['caixa'] = _cache.filter(aberto=True).first()
        return context


class CaixaAbrirView(LoginRequiredMixin, FormView):
    form_class = TransacaoForm
    template_name = "blank.html"

    def form_valid(self, form):
        caixa = Caixa(user=self.request.user)
        caixa.save()
        form.save(caixa=caixa)

        return HttpResponseRedirect(reverse("caixa"), {"form": form})

    def form_invalid(self, form):
        print(form.errors)


class CaixaGetDataView(LoginRequiredMixin, View):
    def get(self, request):
        caixa = buscar_caixa_atual(request.user)
        return JsonResponse(caixa_as_dict(caixa), status=200)


class CaixaFecharView(LoginRequiredMixin, FormView):
    form_class = CaixaFecharForm
    template_name = "blank.html"

    def form_valid(self, form):
        caixa = buscar_caixa_atual(self.request.user)
        caixa_dict = caixa_as_dict(caixa)

        # contar numero de clientes e servicos
        faturas = Fatura.objects.filter(transacao__caixa=caixa)
        if faturas.exists():
            numero_clientes = faturas.values('cliente').distinct().count()
            numero_servicos = faturas.count()
        else:
            numero_clientes = 0
            numero_servicos = 0

        # diferenca do saldo fisico para o saldo total do caixa
        saldo_fisico = float(form.cleaned_data.get("saldo_fisico"))
        dif = saldo_fisico - caixa_dict["budget"]

        # atualizar objeto caixa
        caixa.aberto = False
        caixa.diferenca = dif
        caixa.clientes = numero_clientes
        caixa.servicos = numero_servicos
        caixa.saldo = caixa_dict["budget"]
        caixa.receita = caixa_dict["totals"]["inc"]
        caixa.despesa = caixa_dict["totals"]["exp"]
        caixa.save()

        return HttpResponseRedirect(reverse("caixa"), {"form": form})


class CaixaDeleteAllView(LoginRequiredMixin, View):
    def post(self, request):
        caixa = buscar_caixa_atual(request.user)
        transacoes = Transacao.objects.filter(caixa=caixa)
        if transacoes.exists():
            transacoes.delete()
            return JsonResponse({"message": "Todas as transações do caixa \
                                 atual foram deletadas."}, status=200)
        else:
            return JsonResponse({"message": "O caixa já está vazio!"})


# transações
class TransacaoFormView(LoginRequiredMixin, FormView):
    form_class = TransacaoForm
    template_name = 'blank.html'

    def form_valid(self, form):
        _caixa = buscar_caixa_atual(self.request.user)
        if _caixa:
            obj = form.save(caixa=_caixa)

            return JsonResponse({"object": int(obj.id)}, status=201)
        return JsonResponse({"message": "erro: o caixa não encontrado"},
                            status=404)

    def form_invalid(self, form):
        return JsonResponse(error_response(form.errors, ADD), status=400)


class TransacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Transacao
    success_url = "/"
