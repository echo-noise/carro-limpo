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
        documento = request.POST.get("documento")
        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        placa = request.POST.get("placa")
        cor = request.POST.get("cor")
        marca = request.POST.get("marca")
        modelo = request.POST.get("modelo")

        try:
            cliente = Cliente(documento = documento,
                              nome = nome,
                              telefone = telefone,
                              email = email,
                              placa = placa,
                              cor = cor,
                              marca = marca,
                              modelo = modelo
            )
            cliente.save()
            return JsonResponse({"error": False})

        except:
            return JsonResponse({"error": True})
