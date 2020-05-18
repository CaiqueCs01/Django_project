from django.shortcuts import render, redirect, get_object_or_404
from menu.forms import SaboresForm, MassaForm, TamanhoForm
from .models import Sabores, Massa, TamanhoPizza


def menuC(request):
    return render(request, 'menu/menuC.html')


def menuL(request):
    return render(request, 'menu/menuL.html')


def test_layout(request):
    return render(request, 'menu/base_menu.html')


def sabores_add(request):
    form = SaboresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_sabores')
    return render(request, 'menu/saboresAdd.html', {'form': form})


def sabores_view(request):
    data = {}
    data['sabores'] = Sabores.objects.all()
    return render(request, 'menu/sabores.html', data)


def sabores_up(request, pk):
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
    sabores = Sabores.objects.get(pk=pk)
    sabores.delete()
    return redirect('menu:url_sabores')


def massa_view(request):
    data = {'massa': Massa.objects.all()}
    return render(request, 'menu/massa.html', data)


def massa_add(request):
    form = MassaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_massa')
    return render(request, 'menu/massaAdd.html', {'form': form})


def tamanho_view(request):
    data = {'tamanho': TamanhoPizza.objects.all()}
    return render(request, 'menu/tamanho.html', data)


def tamanho_add(request):
    form = TamanhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_tamanho')
    return render(request, 'menu/tamanhoAdd.html', {'form': form})