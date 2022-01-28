from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="pfp/", blank=True)
    telefone = models.CharField(max_length=15, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Perfil.objects.create(user=instance)


class Loja(models.Model):
    user = models.OneToOneField(User, related_name='loja',
                                on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True)
    cnpj = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Loja.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Endereco(models.Model):
    user = models.OneToOneField(User, related_name='endereco',
                                on_delete=models.CASCADE)
    rua = models.CharField(max_length=100, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=15, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Endereco.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return "{rua} {numero} {complemento}, {bairro}, {cidade} - {uf}, \
                {cep}".format(rua=self.rua, numero=self.numero,
                              complemento=self.complemento, bairro=self.bairro,
                              cidade=self.cidade, uf=self.uf, cep=self.cep)
