from django.urls import path
from . import views
from .views import SaborList, MassaList, TamanhoList

app_name = 'menu'

urlpatterns = [
    path('saboresAdd/', views.sabores_add, name='url_saboresAdd'),
    path('saboresUp/<int:pk>/', views.sabores_up, name='url_saborNovo'),
    path('Sdelete/<int:pk>/', views.sabores_del, name='url_delete'),
    path('massa/', MassaList.as_view(), name='url_massa'),
    path('massaAdd/', views.massa_add, name='url_massaAdd'),
    path('massaUp/<int:pk>/', views.massa_up, name='url_massaUp'),
    path('Mdelete/<int:pk>/', views.massa_del, name='url_massaDel'),
    path('tamanho/', TamanhoList.as_view(), name='url_tamanho'),
    path('tamanhoAdd/', views.tamanho_add, name='url_tamanhoAdd'),
    path('tamanhoUp/<int:pk>/', views.tamanho_up, name='url_tamanhoUp'),
    path('Tdelete/<int:pk>/', views.tamanho_del, name='url_tamanhoDel'),
    path('sabores/', SaborList.as_view(), name="url_sabores"),
]