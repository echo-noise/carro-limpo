from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from .models import Cliente


class ClienteListView(ListView):
    template_name = "clientes.html"
    model = Cliente
    context_object_name = "clientes"

def excluir(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    return redirect("clientes")

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
            return JsonResponse({"error": False}, status=200)

        except:
            return JsonResponse({"error": True}, status=400)
