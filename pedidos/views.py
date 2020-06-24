from django.http import HttpResponse
from django.shortcuts import render, redirect
from menu.models import Sabores, TamanhoPizza
from Pizza.models import CadLojista


def profile(request):
    """Fazer o pedido da pizza."""
    data = {}
    profile_lojista = CadLojista.objects.all()
    data['Lojistas'] = profile_lojista
    return render(request, 'pedidos/menuC.html', data)


def test(request, pk):
    data = {}
    test = CadLojista.objects.get(pk=pk)
    data['test'] = test
    return render(request, 'pedidos/menuC.html', data)

"""
def pedir_view(request):
    data = {}
    context = Sabores.objects.all()
    tamanho = TamanhoPizza.objects.all()
    data['tamanho'] = tamanho
    data['context'] = context
    return render(request, 'pedidos/menuC.html', data)
"""


def procurar_view(request):
    try:
        procurar = request.GET.get('procurar')
    except:
        procurar = None
    if procurar:
        pizza = Sabores.objects.filter(nome__icontains=procurar)
        data = {'busca': procurar, 'pizza': pizza}
        template = 'pedidos/resultados.html'
    else:
        template = 'pedidos/menuC.html'
    return render(request, template, data)


def siderbar(request):
    return render(request, 'pedidos/sidebar.html')