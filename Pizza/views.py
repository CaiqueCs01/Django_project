from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import CreateUserForm, CadConsumidorForm, CadLojistaForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model, get_user


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

                print(request.user.id)
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


def CadLojista(request, pk):
    """Cadastra as informções adicionais do usuário/Lojista"""
    form = CadLojistaForm(request.POST or None)
    #User = get_user_model()
    #print(User.username,'aaaaaaa2')
    #test = User.objects.get(username=get_user(request))
    #print(test,'aaaaaa')
    #print(request.user.id,'usuario')
    if form.is_valid():

        print('aaaa')
        instance = form.save(commit=False)

        instance.user_id = pk
        instance.save()
        return redirect('menu:url_sabores')
    return render(request, "Pizza/CadLojista.html", {'form': form})


def loginView(request):
    """Loga e autentica o usuário através do grupo de permissão."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # loginuser
            user = form.get_user()
            login(request, user)
            group = request.user.groups.filter(user=request.user)[0]
            if group.name == "Lojista":
                return HttpResponseRedirect(reverse('menu:url_sabores'))
            elif group.name == "Consumidor":
                return HttpResponseRedirect(reverse('pedidos:url_profile'))

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