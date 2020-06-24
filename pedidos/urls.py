from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [

    path('procurar/', views.procurar_view, name='url_procurar'),
    path('profile/', views.profile, name='url_profile'),
    path('perfil/<int:pk>/', views.test, name= 'url_perfil'),
    path('sidebar/', views.siderbar)
]

