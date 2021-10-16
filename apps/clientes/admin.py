from django.contrib import admin

from .models import Cliente, Veiculo

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Veiculo)