from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from apps.clientes.models import Cliente
from apps.servicos.models import Servico
from .models import Fatura
from .forms import FaturaForm

# Create your views here.
@login_required
def listar(request):
    template = "faturas.html"

    clientes = Cliente.objects.filter(user=request.user)
    servicos = Servico.objects.filter(user=request.user)
    faturas = Fatura.objects.filter(user=request.user)

    for fatura in faturas:
        print("---")
        print(fatura.cliente.nome)

    return render(request, template, {"clientes": clientes, "servicos": servicos, "faturas": faturas})

@login_required
def salvar(request):
    if request.method == "POST":
        form = FaturaForm(request.POST)
        print(request.POST)

        if form.is_valid():
            fatura = form.save(commit=False)
            fatura.user = request.user
            fatura.save()
            print("fatura salva")

            return HttpResponseRedirect(reverse("faturas"), {"form": form})
        else: 
            print("form invalida")
            return HttpResponseRedirect(reverse("faturas"), {"form": form})

