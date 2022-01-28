from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from carro_limpo.views import UserRequiredCreateView, UpdateViewJson

from .models import Cliente
from .forms import ClienteCreateForm


class ClienteListarView(LoginRequiredMixin, ListView):
    template_name = "clientes.html"
    context_object_name = "clientes"

    def get_queryset(self):
        return Cliente.objects.filter(user=self.request.user)


class ClienteCreateView(LoginRequiredMixin, UserRequiredCreateView):
    form_class = ClienteCreateForm


class ClienteUpdateView(LoginRequiredMixin, UpdateViewJson):
    model = Cliente
    fields = ["nome", "telefone", "email", "documento", "placa", "marca",
              "modelo", "cor"]


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = "/"
