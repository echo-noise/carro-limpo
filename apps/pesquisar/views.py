from django.shortcuts import render
from django.contrib import messages
from django.views.generic import View
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet


# Create your views here.
class SearchAllView(View):
    template_name = "search/search.html"

    def post(self, request):
        queryset = SearchQuerySet().filter(user=self.request.user)
        form = SearchForm(request.POST, searchqueryset=queryset)

        if form.is_valid():
            result = form.search()
            clientes = result.filter(model_verbose="Clientes")
            servicos = result.filter(model_verbose="Servicos")
            faturas = result.filter(model_verbose="Faturas")
            data = {
                "clientes": clientes,
                "servicos": servicos,
                "faturas": faturas
            }
        else:
            messages.error(request, "Ocorreu um erro. Tente novamente.")
            data = {}
        return render(request, self.template_name, data)
