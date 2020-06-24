from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect

from .forms import CreateUserForm, CadConsumidorForm, CadLojistaForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def Registro(request):
    """Registra um novo usuário e coloca ele em um dos grupos de permissões"""
    form = CreateUserForm
    # print(request.POST.get('tipo'))
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username=nome, password=password)
            login(request, account)
            if request.POST.get('tipo') == 'Consumidor':
                myGroup = Group.objects.get(name='Consumidor')
                myGroup.user_set.add(request.user)
                form.save()
                return redirect('Pizza:url_Consumidor')
            else:
                myGroup = Group.objects.get(name='Lojista')
                myGroup.user_set.add(request.user)
                form.save()
                return redirect('Pizza:url_Loj')

    context = {'form': form}
    return render(request, 'Pizza/Registro.html', context)


def CadConsumidor(request):
    """Cadastra as informções adicionais do usuário/Consumidor"""
    data = {}
    form = CadConsumidorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('pedidos:url_profile')
    data['form'] = form
    return render(request, 'Pizza/CadConsumidor.html', data)


def CadLojista(request):
    """Cadastra as informções adicionais do usuário/Lojista"""
    form = CadLojistaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('menu:url_menuL')
    return render(request, "Pizza/CadLojista.html", {'form': form})


def loginView(request):
    """Renderiza a page de login e autentica o usuário."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # loginuser
            user = form.get_user()
            login(request, user)
            grupo = request.user.groups.values_list('name', flat=True)
            print(grupo)
            if grupo == 'Lojista':
                return render(request, 'menu/menuL.html')

    else:
        form = AuthenticationForm()
    return render(request, 'Pizza/login.html', {'form': form})


def home_view(request):
    """Renderiza a page Home"""
    return render(request, 'Pizza/home.html')


def logout_view(request):
    """Faz o logout do usuário"""
    if request.method == 'POST':
        logout(request)
        return redirect('url_home')