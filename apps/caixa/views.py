from django.shortcuts import render
from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from .models import Caixa, Transacao, Despesa
from .forms import TransacaoForm

# Create your views here.
@login_required
def caixa(request):
    template = "caixa.html"
    caixa = Caixa.objects.filter(aberto=True).first()

    return render(request, template, {"caixa": caixa})

@login_required
def abrir_caixa(request):
    if request.method == "POST":
        form = TransacaoForm(request.POST)

        if form.is_valid():
            caixa = Caixa(user=request.user)
            caixa.save()

            entrada = form.save(commit=False)
            entrada.caixa = caixa
            entrada.description = "Valor Inicial"
            entrada.save()
        else: 
            print("form invalida.")
            print(form.errors)

        return HttpResponseRedirect(reverse("caixa"), {"form": form})

def get_caixa(request):
    caixa = Caixa.objects.filter(aberto=True).first()
    if request.method == "GET":
        inc = []
        exp = []

        receitas = Transacao.objects.filter(caixa=caixa)
        
        if receitas:
            for receita in receitas:
                inc.append({"id": receita.applet_id, "value": receita.value, "description": receita.description})
        
        despesas = Despesa.objects.filter(caixa = caixa)
        
        if despesas:
            for despesa in despesas:
                exp.append({"id": despesa.applet_id, 
                            "value": despesa.value, 
                            "description": despesa.description, 
                            "percentage": despesa.percentage}
                            )
            despesas_total = despesas.aggregate(Sum('value'))
            despesas_total = float(despesas_total['value__sum'])
            percentage = despesas.aggregate(Sum('percentage'))
            percentage = int(percentage['percentage__sum'])
        else: 
            despesas_total = 0
            percentage = 0
        
        receitas_total = receitas.aggregate(Sum('value'))
        receitas_total = float(receitas_total['value__sum'])

        budget = receitas_total - despesas_total

        data = {
            "allItems": {"exp": exp, "inc": inc},
            "totals": {"exp": despesas_total, "inc": receitas_total},
            "budget": budget,
            "percentage": percentage
        }

        return JsonResponse(data, status=200)



