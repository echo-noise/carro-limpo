from django.contrib.auth import login
from django.http.response import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Servico
from .forms import ServicoForm

# Create your views here.
@login_required
def listar(request):
    template = "servicos.html"
    servicos = Servico.objects.filter(user = request.user)
    return render(request, template, {"servicos": servicos})

@login_required
@csrf_exempt
def inserir(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)

        if form.is_valid():
            servico = form.save(commit=False)
            servico.user = request.user
            servico.save()

            response = { 
                "id": servico.id,
                "nome": servico.nome,
                "valor": servico.valor,
                "error": False,
                "message": "Adicionar: sucesso"
            }
            return JsonResponse(response, status=200, safe=False)

        return JsonResponse({"error": True, "message": "Adicionar: erro"}, status=400)

@login_required
@csrf_exempt
def excluir(request, id):
    if request.method == 'POST':
        if id == -1:
            response = {"error": False, "message": "Deletar: vazio"}
            return JsonResponse(response, status=200, safe=False)

        try:
            servico = get_object_or_404(Servico, pk=id) 
            servico.delete()
            response = {"error": False, "message": "Deletar: sucesso"}
            return JsonResponse(response, status=200, safe=False)
        except:
            response = {"error": True, "message": "Deletar: erro"}
            return JsonResponse(response, status=400, safe=False)

@login_required
@csrf_exempt
def atualizar(request, id):
    if request.method == "POST":
        servico = get_object_or_404(Servico, pk=id)
        form = ServicoForm(request.POST, instance=servico)

        if form.is_valid():
            form.save()
            response = {"error": False, "message": "Atualizar: sucesso"}
            
            return JsonResponse(response, status=200, safe=False)

        response = {"error": True, "message": "Atualizar: erro"}
        return JsonResponse(response, status=400, safe=False) 