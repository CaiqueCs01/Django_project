from django.contrib.auth.models import User
from django.db import models
from Pizza.models import CadLojista


class Sabores(models.Model):
    nome         = models.CharField(max_length=20)
    ingredientes = models.CharField(max_length=300)
    preco        = models.DecimalField(decimal_places=2, max_digits=10, default=29.99)
    image        = models.ImageField(upload_to='static/images/', blank=True)
    lojistas_id     = models.ForeignKey(CadLojista, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    def get_preco(self):
        return self.preco


class Massa(models.Model):
    tipo = models.CharField(max_length=30, verbose_name="Tipo de Massa")
    lojistas_id = models.ForeignKey(CadLojista, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo


class TamanhoPizza(models.Model):
    tamanho = models.CharField(max_length=30)
    lojistas_id = models.ForeignKey(CadLojista, default=None, on_delete= models.CASCADE)

    def __str__(self):
        return self.tamanho


