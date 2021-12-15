from django.shortcuts import render

# Create your views here.
def listar(request):
    template = "caixa.html"
    return render(request, template)