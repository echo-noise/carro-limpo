from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Servico

# Create your views here.
def listar(request):
    template = "servicos.html"
    servicos = Servico.objects.all()
    return render(request, template, {"servicos": servicos})

@csrf_exempt
def inserir(request):
    if request.method == 'POST':
        _nome = request.POST.get("nome")
        _valor = request.POST.get("valor")

        try:
            servico = Servico(nome = _nome,
                              valor = _valor
                              )
            servico.save()
            response = { 
                "id": servico.id,
                "nome": servico.nome,
                "valor": servico.valor,
                "error": False,
                "message": "Adicionar: sucesso"
            }
            return JsonResponse(response, status=200, safe=False)
        except:
            return JsonResponse({"error": True, "message": "Adicionar: erro"}, status=400)

@csrf_exempt
def excluir(request, id):
    if request.method == 'POST':
        if id == -1:
            response = {"error": False, "message": "Deletar: vazio"}
            return JsonResponse(response, status=200, safe=False)
        else:
            try:
                servico = Servico.objects.get(pk=id)
                servico.delete()
                response = {"error": False, "message": "Deletar: sucesso"}
                return JsonResponse(response, status=200, safe=False)
            except:
                response = {"error": True, "message": "Deletar: erro"}
                return JsonResponse(response, status=400, safe=False)

@csrf_exempt
def atualizar(request, id):
    if request.method == "POST":
        _nome = request.POST.get("nome")
        _valor = request.POST.get("valor")
        try:
            servico = Servico.objects.get(pk=id)
            servico.nome = _nome 
            servico.valor = _valor

            servico.save()
            response = {"error": False, "message": "Atualizar: sucesso"}
            
            return JsonResponse(response, status=200, safe=False)
        except:
            response = {"error": True, "message": "Atualizar: erro"}
            return JsonResponse(response, status=400, safe=False) 