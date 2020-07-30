

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404

from Pizza.models import CadLojista
from menu.forms import SaboresForm, MassaForm, TamanhoForm
from .models import Sabores, Massa, TamanhoPizza
from django.contrib.auth.decorators import login_required


@login_required(login_url='Pizza:url_login')
def sabores_add(request):
    "Adiciona um sabor novo ao cardápio"
    form = SaboresForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        test = CadLojista.objects.get(nome=request.user)
        instance.lojistas_id_id = test.id

        instance.save()
        return redirect('menu:url_sabores')
    return render(request, 'menu/saboresAdd.html', {'form': form})


class SaborList(LoginRequiredMixin, ListView):

    model = Sabores

    template_name = 'menu/sabores2.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        test = CadLojista.objects.get(nome=self.request.user)
        print(test.id)
        self.object_list = Sabores.objects.filter(lojistas_id_id=test.id)

        print(self.request.user.id)

        return self.object_list


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


class MassaList(LoginRequiredMixin, ListView):
    model = Massa
    template_name = 'menu/massa.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView

        self.object_list = Massa.objects.filter(lojistas_id=self.request.user.id)

        return self.object_list

"""
o id do lojista tem que passa para a FK de sabores
"""
@login_required(login_url='Pizza:url_login')
def massa_add(request):
    """Adiciona uma massa nova ao cardápio"""
    form = MassaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.lojistas_id_id = request.user.id
        instance.save()
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


class TamanhoList(LoginRequiredMixin, ListView):
    model = TamanhoPizza
    template_name = 'menu/tamanho.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView

        self.object_list = TamanhoPizza.objects.filter(lojistas_id=self.request.user.id)

        return self.object_list



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
        instance = form.save(commit=False)
        instance.lojistas_id_id = request.user.id
        instance.save()
        return redirect('menu:url_tamanho')
    return render(request, 'menu/tamanhoAdd.html', {'form': form})


def tamanho_del(request, pk):
    """Deleta um tamanho de pizza."""
    tamanho = TamanhoPizza.objects.get(pk=pk)
    tamanho.delete()
    return redirect('menu:url_tamanho')