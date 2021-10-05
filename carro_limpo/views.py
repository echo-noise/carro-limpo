from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def clientes(request):
    return render(request, "clientes.html")