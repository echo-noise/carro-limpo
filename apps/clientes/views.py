from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Cliente
from .forms import ClienteForm

@login_required
def listar(request):
    template = "clientes.html"
    clientes = Cliente.objects.filter(user = request.user)
    return render(request, template, {"clientes": clientes})

@login_required
@csrf_exempt
def inserir(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user
            cliente.save()

            response = { 
                "id": cliente.id,
                "error": False,
                "message": "Adicionar: sucesso"
            }
            return JsonResponse(response, status=200, safe=False)
        else:
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
                cliente = get_object_or_404(Cliente, pk=id) 
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
        cliente = get_object_or_404(Cliente, pk=id)
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            response = {"error": False, "message": "Atualizar: sucesso"}
            
            return JsonResponse(response, status=200, safe=False)
        else:
            response = {"error": True, "message": "Atualizar: erro"}
            return JsonResponse(response, status=400, safe=False) 