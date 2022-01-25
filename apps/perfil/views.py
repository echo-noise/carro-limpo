from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

from .forms import UserEditForm, LojaForm, ImageForm, EnderecoForm, UserProfileForm

# Create your views here.
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = "administrador.html"

    def user_profile_forms(self, request):
        forms = []
        user_form = UserEditForm(request.POST, instance=self.request.user)
        user_form_extended = UserProfileForm(request.POST, instance=self.request.user.profile)
        password_form = PasswordChangeForm(self.request.user)

        forms.append(user_form)
        forms.append(user_form_extended)

        if(request.POST.get("old_password")):
            password_form = PasswordChangeForm(self.request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.add_message(request, messages.INFO, "Senha alterada.")

        for form in forms:
            if form.is_valid():
                form.save()
        
        response = { 
            "user_form": user_form,
            "user_form_extended": user_form_extended,
            "password_form": password_form
        }

        return response

    def loja_forms(self, request):
        form = LojaForm(request.POST, instance=request.user.loja)
        form_endereco = EnderecoForm(request.POST, instance=request.user.endereco)

        if form.is_valid() and form_endereco.is_valid():
            form.save()
            form_endereco.save()
        
        response = { "loja_form": form,
                     "endereco_form": form_endereco
                   }
        return response

    def post(self, request, *args, **kwargs):
        if int(request.POST.get("form-id")) == 0:
            return self.render_to_response(self.user_profile_forms(request))
        elif int(request.POST.get("form-id")) == 1:
            return self.render_to_response(self.loja_forms(request))

@login_required
def salvar_imagem(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'}, status=200)

        return JsonResponse({'error': True, 'errors': form.errors, 'message':'form inválida'}, status=400)
    