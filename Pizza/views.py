from django.contrib.auth.models import Group
from django.urls import reverse

from .forms import CreateUserForm, CadConsumidorForm, CadLojistaForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


def Registro(request):
    form = CreateUserForm
    #print(request.POST.get('tipo'))
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get('tipo') == 'Consumidor':
                myGroup = Group.objects.get(name='Consumidor')
                print(myGroup)
                print(request.user)
                myGroup.user_set.add(request.user)
                form.save()
                return redirect('Pizza:url_Consu')
            else:
                myGroup = Group.objects.get(name='Lojista')
                myGroup.user_set.add(request.user)
                form.save()
                return redirect('Pizza:url_Loj')

    context = {'form': form}
    return render(request, 'Pizza/Registro.html', context)


def CadConsumidor(request):
    data = {}
    form = CadConsumidorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('menu:url_menuC')
    data['form'] = form
    return render(request, 'Pizza/CadConsumidor.html', data)


def CadLojista(request):
    form = CadLojistaForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('menu:url_menuL')
    return render(request, "Pizza/CadLojista.html", {'form': form})


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #loginuser
            user = form.get_user()
            login(request, user)
            return redirect('url_home')
    else:
        form = AuthenticationForm()
    return render(request, 'Pizza/login.html', {'form': form})


def home_view(request):
    return render(request, 'Pizza/home.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('url_home')

