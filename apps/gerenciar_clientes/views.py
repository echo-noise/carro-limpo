from django.shortcuts import render

# Create your views here.
def clientes(request):
    template = "clientes.html"
    return render(request, template)