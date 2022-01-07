from .models import Caixa

def buscar_caixa_atual(user):
    return Caixa.objects.filter(user=user, aberto=True).first()