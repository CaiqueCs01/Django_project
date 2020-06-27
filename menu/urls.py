from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('sabores/', views.sabores_view, name='url_sabores'),
    path('saboresAdd/', views.sabores_add, name='url_saboresAdd'),
    path('saboresUp/<int:pk>/', views.sabores_up, name='url_saborNovo'),
    path('Sdelete/<int:pk>/', views.sabores_del, name='url_delete'),
    path('massa/', views.massa_view, name='url_massa'),
    path('massaAdd/', views.massa_add, name='url_massaAdd'),
    path('massaUp/<int:pk>/', views.massa_up, name='url_massaUp'),
    path('Mdelete/<int:pk>/', views.massa_del, name='url_massaDel'),
    path('tamanho/', views.tamanho_view, name='url_tamanho'),
    path('tamanhoAdd/', views.tamanho_add, name='url_tamanhoAdd'),
    path('tamanhoUp/<int:pk>/', views.tamanho_up, name='url_tamanhoUp'),
    path('Tdelete/<int:pk>/', views.tamanho_del, name='url_tamanhoDel'),
]