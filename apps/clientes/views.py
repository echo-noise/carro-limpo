from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from carro_limpo.views import UserRequiredCreateView, UserRequiredUpdateView

from .models import Cliente
from .forms import ClienteForm, ClienteCreateForm

class ClienteListarView(LoginRequiredMixin, ListView):
    template_name = "clientes.html"
    context_object_name = "clientes"

    def get_queryset(self):
        return Cliente.objects.filter(user=self.request.user)

class ClienteCreateView(LoginRequiredMixin, UserRequiredCreateView):
    form_class = ClienteCreateForm

class ClienteUpdateView(LoginRequiredMixin, UserRequiredUpdateView):
    model = Cliente
    form_class = ClienteForm
    
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = "/"