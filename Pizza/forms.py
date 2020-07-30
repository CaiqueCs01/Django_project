from django.contrib.auth.forms import forms, UserCreationForm
from django.contrib.auth.models import User

from Pizza.models import CadConsumidor, CadLojista


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
            'email': None,
            'password1': 'asasa',
            'password2': 'saksikas',

        }


class CadConsumidorForm(forms.ModelForm):
    nome     = forms.CharField(max_length=50)
    endereço = forms.CharField(max_length=100)
    bairro   = forms.CharField(max_length=50)
    cidade   = forms.CharField(max_length=50)

    class Meta:
        model  = CadConsumidor
        fields = ['nome', 'endereço', 'bairro', 'cidade']


class CadLojistaForm(forms.ModelForm):
    nome         = forms.CharField(max_length=50)
    nomePizzaria = forms.CharField(max_length=50)
    endereço     = forms.CharField(max_length=100)
    bairro       = forms.CharField(max_length=50)
    cidade       = forms.CharField(max_length=50)
    diaFuncional = forms.CharField(max_length=50)
    horaInicio   = forms.DateTimeInput()
    horaFinal    = forms.DateTimeInput()

    class Meta:
        model = CadLojista
        fields = ['nome', 'nomePizzaria','endereço',
                  'bairro', 'cidade', 'diaFuncional',
                  'horaInicio', 'horaFinal']


