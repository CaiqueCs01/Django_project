from django.shortcuts import render, redirect, get_object_or_404
from menu.forms import SaboresForm, MassaForm, TamanhoForm
from .models import Sabores, Massa, TamanhoPizza
from django.contrib.auth.decorators import login_required


@login_required(login_url='Pizza:url_login')
def sabores_add(request):
    """Adiciona um sabor novo ao cardápio"""
    form = SaboresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_sabores')
    return render(request, 'menu/saboresAdd.html', {'form': form})


@login_required(login_url='Pizza:url_login')
def sabores_view(request):
    """Mostra a lista de sabores salvos no banco de dados."""
    data = {}
    data['sabores'] = Sabores.objects.all()
    return render(request, 'menu/sabores.html', data)


@login_required(login_url='Pizza:url_login')
def sabores_up(request, pk):
    """Permite o usuário fazer alterações nas pizzas e ingredientes."""
    data = {}
    saborNovo = Sabores.objects.get(pk=pk)
    form = SaboresForm(request.POST or None, instance=saborNovo)
    if form.is_valid():
        form.save()
        return redirect('menu:url_sabores')
    data['form'] = form
    data['sabores'] = saborNovo
    return render(request, 'menu/saboresAdd.html', data)


def sabores_del(request, pk):
    """Deleta um sabor."""
    sabores = Sabores.objects.get(pk=pk)
    sabores.delete()
    return redirect('menu:url_sabores')


@login_required(login_url='Pizza:url_login')
def massa_view(request):
    """Mostra a lista de tipos de massas salvos no banco de dados."""
    data = {'massa': Massa.objects.all()}
    return render(request, 'menu/massa.html', data)


@login_required(login_url='Pizza:url_login')
def massa_add(request):
    """Adiciona uma massa nova ao cardápio"""
    form = MassaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_massa')
    return render(request, 'menu/massaAdd.html', {'form': form})


@login_required(login_url='Pizza:url_login')
def massa_up(request, pk):
    """Permite o usuário fazer alterações nas massas."""
    data = {}
    massaNovo = Massa.objects.get(pk=pk)
    form = MassaForm(request.POST or None, instance=massaNovo)
    if form.is_valid():
        form.save()
        return redirect('menu:url_massa')
    data['form'] = form
    data['massa'] = massaNovo
    return render(request, 'menu/massaAdd.html', data)


def massa_del(request, pk):
    """Deleta um tipo massa."""
    massa = Massa.objects.get(pk=pk)
    massa.delete()
    return redirect('menu:url_massa')


@login_required(login_url='Pizza:url_login')
def tamanho_view(request):
    """Mostra a lista de tamanhos salvos no banco de dados."""
    data = {'tamanho': TamanhoPizza.objects.all()}
    return render(request, 'menu/tamanho.html', data)


@login_required(login_url='Pizza:url_login')
def tamanho_up(request, pk):
    """Permite o usuário fazer alterações nos tamanhos das pizzas."""
    data = {}
    tamanhoNovo = TamanhoPizza.objects.get(pk=pk)
    form = TamanhoForm(request.POST or None, instance=tamanhoNovo)
    if form.is_valid():
        form.save()
        return redirect('menu:url_tamanho')
    data['form'] = form
    data['tamanho'] = tamanhoNovo
    return render(request, 'menu/tamanhoAdd.html', data)


@login_required(login_url='Pizza:url_login')
def tamanho_add(request):
    """Adiciona um tamanho novo ao cardápio"""
    form = TamanhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_tamanho')
    return render(request, 'menu/tamanhoAdd.html', {'form': form})


def tamanho_del(request, pk):
    """Deleta um tamanho de pizza."""
    tamanho = TamanhoPizza.objects.get(pk=pk)
    tamanho.delete()
    return redirect('menu:url_tamanho')