from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from carro_limpo.views import UserRequiredCreateView, UpdateViewJson

from .models import Servico
from .forms import ServicoCreateForm


class ServicoListarView(LoginRequiredMixin, ListView):
    template_name = "servicos.html"
    context_object_name = "servicos"

    def get_queryset(self):
        return Servico.objects.filter(user=self.request.user)


class ServicoCreateView(LoginRequiredMixin, UserRequiredCreateView):
    form_class = ServicoCreateForm


class ServicoUpdateView(LoginRequiredMixin, UpdateViewJson):
    model = Servico
    fields = ("nome", "valor")


class ServicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Servico
    success_url = "/"
