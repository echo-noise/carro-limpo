from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Veiculo

class ListarVeiculoView(ListView):
    template_name = "clientes.html"
    model = Veiculo
    context_object_name = "veiculos"

def excluir(request, id):
    veiculo = Veiculo.objects.get(pk=id)
    veiculo.delete()
    return redirect("clientes")