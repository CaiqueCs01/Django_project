from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class CadConsumidor(models.Model):
    nome     = models.CharField(max_length=50)
    endereço = models.CharField(max_length=100)
    bairro   = models.CharField(max_length=50)
    cidade   = models.CharField(max_length=50)
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class CadLojista(models.Model):
    nome         = models.CharField(max_length=50)
    nomePizzaria = models.CharField(max_length=50, verbose_name='Nome da Pizzaria!')
    endereço     = models.CharField(max_length=100)
    bairro       = models.CharField(max_length=50)
    cidade       = models.CharField(max_length=50)
    diaFuncional = models.CharField(max_length=100, verbose_name='Dias de Funcinamento')
    horaInicio   = models.CharField(max_length=5, verbose_name='Hora de Início')
    horaFinal    = models.CharField(max_length=5, verbose_name='Horário de Fechamento')
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome




