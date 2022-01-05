from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from apps.clientes.models import Cliente
from apps.servicos.models import Servico
from .models import Fatura
from .forms import FaturaEditForm, FaturaForm

# Create your views here.
@login_required
def listar(request):
    template = "faturas.html"

    clientes = Cliente.objects.filter(user=request.user)
    servicos = Servico.objects.filter(user=request.user)
    faturas = Fatura.objects.filter(user=request.user)

    return render(request, template, {"clientes": clientes, "servicos": servicos, "faturas": faturas})

@login_required
def salvar(request):
    if request.method == "POST":
        form = FaturaForm(request.POST)

        if form.is_valid():
            fatura = form.save(commit=False)
            fatura.user = request.user
            fatura.save()
            print("fatura salva")

            return HttpResponseRedirect(reverse("faturas"), {"form": form})
        else: 
            print("form invalida")
            return HttpResponseRedirect(reverse("faturas"), {"form": form})

@login_required
def gerar(request, id):
    if request.method == "GET":
        fatura = get_object_or_404(Fatura, pk=id)
        print (fatura.pago)

        if fatura:
            if not fatura.pago:
                _status = "Pendente"
                fatura.pago = True
                fatura.save()
            else:
                _status = "Pago"

            response = { 
                "cliente_nome": fatura.cliente.nome,
                "cliente_tel": fatura.cliente.telefone,
                "cliente_email": fatura.cliente.email,
                "cliente_documento": fatura.cliente.documento,
                "cliente_marca": fatura.cliente.marca,
                "cliente_modelo": fatura.cliente.modelo,
                "cliente_placa": fatura.cliente.placa,
                "servico_nome": fatura.servico.nome,
                "servico_valor": fatura.servico.valor,
                "loja_rs": request.user.loja.nome,
                "loja_tel": request.user.loja.telefone,
                "loja_cnpj": request.user.loja.cnpj,
                "loja_email": request.user.loja.email,
                "loja_endereco": str(request.user.endereco),
                "fatura_valor": fatura.servico.valor,
                "fatura_data": fatura.data,
                "fatura_status": _status
            }

            return JsonResponse(response, status=200)
        else: 
            return JsonResponse(status=400)

@login_required
def excluir(request, id):
    if request.method == 'POST':
        try:
            fatura = get_object_or_404(Fatura, pk=id) 
            fatura.delete()
            response = {"error": False, "message": "Deletar: sucesso"}
            return JsonResponse(response, status=200, safe=False)
        except:
            response = {"error": True, "message": "Deletar: erro"}
            return JsonResponse(response, status=400, safe=False)

@login_required
def atualizar(request, id):
    if request.method == "POST":
        fatura = get_object_or_404(Fatura, pk=id)
        form = FaturaEditForm(request.POST, instance=fatura)

        if form.is_valid():
            form.save()
            response = {"error": False, "message": "Atualizar: sucesso"}
            
            return JsonResponse(response, status=200, safe=False)
        else:
            response = {"error": True, "message": "Atualizar: erro"}
            return JsonResponse(response, status=400, safe=False) 