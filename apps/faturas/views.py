from django.shortcuts import render

# Create your views here.
def listar(request):
    template = "faturas.html"
    return render(request, template)