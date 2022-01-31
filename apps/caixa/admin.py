from django.contrib import admin

from .models import Caixa, Transacao

# Register your models here.
admin.site.register(Caixa)
admin.site.register(Transacao)