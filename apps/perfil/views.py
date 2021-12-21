from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .forms import UserProfileForm, EstabelecimentoForm, ImageForm

# Create your views here.
@login_required
def perfil(request):
    template = "administrador.html"

    perfil = request.user.profile

    return render(request, template, {"perfil": perfil})

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
            request.user.profile.telefone_usuario = (_fone) 

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
        form = EstabelecimentoForm(request.POST)

        if form.is_valid():
            _razao = form.cleaned_data.get(("name"))
            _cnpj = form.cleaned_data.get(("cnpj"))
            _telefone = form.cleaned_data.get(("telefone"))
            _email = form.cleaned_data.get(("email"))
            _cep = form.cleaned_data.get(("cep"))
            _endereco = form.cleaned_data.get(("endereco"))
            _numero = form.cleaned_data.get(("numero"))
            _complemento = form.cleaned_data.get(("complemento"))
            _bairro = form.cleaned_data.get(("bairro"))
            _cidade = form.cleaned_data.get(("cidade"))
            _estado = form.cleaned_data.get(("estado"))

            request.user.profile.razao_social = _razao
            request.user.profile.cnpj = _cnpj
            request.user.profile.telefone = _telefone
            request.user.profile.email_negocio = _email
            request.user.profile.cep = _cep
            request.user.profile.endereco = _endereco
            request.user.profile.complemento = _complemento
            request.user.profile.numero = _numero
            request.user.profile.bairro = _bairro
            request.user.profile.cidade = _cidade
            request.user.profile.uf = _estado

            request.user.save()

        return HttpResponseRedirect(reverse("perfil"), {"form": form, "active": "#profile"})

@login_required
@csrf_exempt
def salvar_imagem(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            request.user.profile.imagem = form.cleaned_data.get("imagem")
            request.user.save()
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'}, status=200)

        return JsonResponse({'error': True, 'errors': form.errors, 'message':'form inválida'}, status=400)
    