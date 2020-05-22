from django.db import models
from menu.models import Sabores, Massa, TamanhoPizza


class PedirPizza(models.Model):
    id_sabor   = models.ForeignKey(Sabores, default=None, on_delete=models.CASCADE)
    id_tipo    = models.ForeignKey(Massa, default=None, on_delete=models.CASCADE)
    id_tamanho = models.ForeignKey(TamanhoPizza, default=None, on_delete=models.CASCADE)
