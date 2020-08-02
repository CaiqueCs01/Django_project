from django.urls import path
from . import views

app_name = 'Pizza'

urlpatterns = [
    path('Registro/', views.Registro, name='url_Registro'),
    path('CadConsumidor/', views.CadConsumidor, name='url_Consumidor'),
    path('CadLojista/<int:pk>/', views.Cad_Lojista, name='url_Loj'),
    path('Login/', views.loginView, name='url_login'),
    path('Logout/', views.logout_view, name='url_logout'),
]