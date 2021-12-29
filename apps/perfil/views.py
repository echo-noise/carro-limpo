from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm, LojaForm, ImageForm, EnderecoForm

# Create your views here.
@login_required
def perfil(request):
    template = "administrador.html"

    return render(request, template)

@login_required
def salvar_perfil(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, request=request)

        if form.is_valid():
            _name = form.cleaned_data.get("user_name")
            _email = form.cleaned_data.get("user_email")
            _fone = form.cleaned_data.get("user_fone")

            request.user.first_name = _name
            request.user.email = _email
            request.user.profile.telefone = (_fone) 

            _new_password = form.cleaned_data.get("new_password")
            
            if _new_password:
                request.user.set_password(_new_password)

            request.user.save()
        else:
            print(form.errors)
        
        return HttpResponseRedirect(reverse("perfil"), {"form": form})

@login_required
def salvar_estabelecimento(request):
    if request.method == "POST":
        form = LojaForm(request.POST, instance=request.user.loja)
        form_endereco = EnderecoForm(request.POST, instance=request.user.endereco)

        if form.is_valid() and form_endereco.is_valid():
            form.save()
            form_endereco.save()

        return HttpResponseRedirect(reverse("perfil"), {"form": form, "active": "#profile"})

@login_required
def salvar_imagem(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'}, status=200)

        return JsonResponse({'error': True, 'errors': form.errors, 'message':'form inválida'}, status=400)
    