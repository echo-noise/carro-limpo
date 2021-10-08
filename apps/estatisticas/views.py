from django.shortcuts import render

def home(request):
    template = "index.html"
    return render(request, template)
