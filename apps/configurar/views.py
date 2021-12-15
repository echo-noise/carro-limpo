from django.shortcuts import render

# Create your views here.
def configurar(request):
    template = "administrador.html"
    return render(request, template)