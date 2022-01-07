from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect, JsonResponse
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView


from .models import Caixa, Transacao
from .forms import TransacaoForm, TransacaoBaseForm
from .helper import buscar_caixa_atual

# Create your views here.
@login_required
def caixa(request):
    template = "caixa.html"
    caixa = Caixa.objects.filter(aberto=True).first()

    return render(request, template, {"caixa": caixa})

@login_required
def abrir_caixa(request):
    if request.method == "POST":
        form = TransacaoBaseForm(request.POST)

        if form.is_valid():
            caixa = Caixa(user=request.user)
            caixa.save()

            entrada = form.save(commit=False)
            entrada.caixa = caixa
            entrada.description = "Valor Inicial"
            entrada.type = 'inc'
            entrada.save()
        else: 
            print("form invalida.")
            print(form.errors)

        return HttpResponseRedirect(reverse("caixa"), {"form": form})

class CaixaGetDataView(LoginRequiredMixin, View):
    def get(self, request):
        _caixa = buscar_caixa_atual(request.user) 

        if _caixa:
            inc = []
            exp = []

            _cache = Transacao.objects.filter(caixa=_caixa)
            receitas = _cache.filter(type='inc')
        
            if receitas.exists():
                for receita in receitas:
                    inc.append({"id": int(receita.id), 
                                "value": float(receita.value), 
                                "description": receita.description})            
                receitas_total = receitas.aggregate(Sum('value'))
                receitas_total = float(receitas_total['value__sum'])
            else:
                receitas_total = 0

            despesas = _cache.filter(type='exp')
        
            if despesas.exists():
                for despesa in despesas:
                    exp.append({"id": int(despesa.id),
                                "value": float(despesa.value), 
                                "description": despesa.description, 
                                 }
                                )
                despesas_total = despesas.aggregate(Sum('value'))
                despesas_total = float(despesas_total['value__sum'])
                percentage = round(despesas_total / receitas_total * 100)
            else: 
                despesas_total = 0
                percentage = 0

            budget = receitas_total - despesas_total

            data = {
                "allItems": {"exp": exp, "inc": inc},
                "totals": {"exp": despesas_total, "inc": receitas_total},
                "budget": budget,
                "percentage": percentage
            }

            return JsonResponse(data, status=200)
        return JsonResponse({}, status=404)

class TransacaoFormView(LoginRequiredMixin, FormView):
    form_class = TransacaoForm
    template_name = 'blank.html'

    def form_valid(self, form):
        _caixa = buscar_caixa_atual(self.request.user)
        if _caixa:
            form.save(caixa=_caixa)
            
            return JsonResponse(form.cleaned_data, status=200)
        return JsonResponse(form.cleaned_data, status=404)

    def form_invalid(self, form):
        return JsonResponse(form.errors.as_json(), status=400, safe=False)

class TransacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Transacao
    success_url = "/"
