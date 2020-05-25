from django.shortcuts import render
from menu.models import Sabores, TamanhoPizza


def pedir_view(request):
    """Fazer o pedido da pizza."""
    data = {}
    context = Sabores.objects.all()
    tamanho = TamanhoPizza.objects.all()
    data['tamanho'] = tamanho
    data['context'] = context
    return render(request, 'pedidos/menuC.html', data)


