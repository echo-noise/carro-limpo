from django.http.response import JsonResponse
from django.views.generic import UpdateView, CreateView

from .helper import ADD, EDIT, DELETE, default_response, error_response

class UserRequiredCreateView(CreateView):
    def form_valid(self, form):
        obj = form.save(self.request.user)
        return JsonResponse(default_response(obj, ADD), status=201)
    
    def form_invalid(self, form):
        return JsonResponse(error_response(form.errors, ADD), status=400)

class UserRequiredUpdateView(UpdateView):
    def form_valid(self, form):
        obj = form.save()
        return JsonResponse(default_response(obj, EDIT), status=200)
    
    def form_invalid(self, form):
        return JsonResponse(error_response(form.errors, EDIT), status=400)


