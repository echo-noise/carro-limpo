from django.contrib.auth import login
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Cliente
#class ClienteListView(ListView):
#    template_name = "clientes.html"
#    model = Cliente
#    context_object_name = "clientes"

@login_required
def listar(request):
    template = "clientes.html"
    clientes = Cliente.objects.all()
    return render(request, template, {"clientes": clientes})

@login_required
@csrf_exempt
def inserir(request):
    if request.method == 'POST':
        _documento = request.POST.get("documento")
        _nome = request.POST.get("nome")
        _telefone = request.POST.get("telefone")
        _email = request.POST.get("email")
        _placa = request.POST.get("placa")
        _cor = request.POST.get("cor")
        _marca = request.POST.get("marca")
        _modelo = request.POST.get("modelo")

        try:
            cliente = Cliente(documento = _documento,
                              nome = _nome,
                              telefone = _telefone,
                              email = _email,
                              placa = _placa,
                              cor = _cor,
                              marca = _marca,
                              modelo = _modelo
            )
            cliente.save()
            response = { 
                "id": cliente.id,
                "nome": cliente.nome,
                "documento": cliente.documento,
                "telefone": cliente.telefone,
                "email": cliente.email,
                "placa": cliente.placa,
                "cor": cliente.cor,
                "marca": cliente.marca,
                "modelo": cliente.modelo,
                "error": False,
                "message": "Adicionar: sucesso"
            }
            return JsonResponse(response, status=200, safe=False)
        except:
            return JsonResponse({"error": True, "message": "Adicionar: erro"}, status=400)

@login_required
@csrf_exempt
def excluir(request, id):
    if request.method == 'POST':
        if id == -1:
            response = {"error": False, "message": "Deletar: vazio"}
            return JsonResponse(response, status=200, safe=False)
        else:
            try:
                cliente = Cliente.objects.get(pk=id)
                cliente.delete()
                response = {"error": False, "message": "Deletar: sucesso"}
                return JsonResponse(response, status=200, safe=False)
            except:
                response = {"error": True, "message": "Deletar: erro"}
                return JsonResponse(response, status=400, safe=False)

@login_required
@csrf_exempt
def atualizar(request, id):
    if request.method == "POST":
        _documento = request.POST.get("documento")
        _nome = request.POST.get("nome")
        _telefone = request.POST.get("telefone")
        _email = request.POST.get("email")
        _placa = request.POST.get("placa")
        _cor = request.POST.get("cor")
        _marca = request.POST.get("marca")
        _modelo = request.POST.get("modelo")
        try:
            cliente = Cliente.objects.get(pk=id)
            cliente.nome = _nome 
            cliente.telefone = _telefone
            cliente.email = _email
            cliente.documento = _documento
            cliente.placa = _placa
            cliente.marca = _marca
            cliente.modelo = _modelo
            cliente.cor = _cor
            
            cliente.save()
            response = {"error": False, "message": "Atualizar: sucesso"}
            
            return JsonResponse(response, status=200, safe=False)
        except:
            response = {"error": True, "message": "Atualizar: erro"}
            return JsonResponse(response, status=400, safe=False) 