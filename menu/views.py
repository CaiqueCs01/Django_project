from django.shortcuts import render, redirect
from menu.forms import SabooresForm, MassaForm, TamanhoForm


def menuC(request):
    return render(request, 'menu/menuC.html')


def menuL(request):
    return render(request, 'menu/menuL.html')


def test_layout(request):
    return render(request, 'menu/base_menu.html')


def sabores_view(request):
    form = SabooresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_sabores')
    return render(request, 'menu/sabores.html', {'form': form})


def massa_view(request):
    form = MassaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_massa')
    return render(request, 'menu/massa.html', {'form': form})


def tamanho_view(request):
    form = TamanhoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('menu:url_tamanho')
    return render(request, 'menu/tamanho.html', {'form': form})