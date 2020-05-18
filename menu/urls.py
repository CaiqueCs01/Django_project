from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('menuC/', views.menuC, name='url_menuC'),
    path('menuL/', views.menuL, name='url_menuL'),
    path('test/', views.test_layout, name='url_test'),
    path('sabores/', views.sabores_view, name='url_sabores'),
    path('massa/', views.massa_view, name='url_massa'),
    path('tamanho/', views.tamanho_view, name='url_tamanho'),
    path('saboresAdd/', views.sabores_add, name='url_saboresAdd'),
    path('massaAdd/', views.massa_add, name='url_massaAdd'),
    path('tamanhoAdd/', views.tamanho_add, name='url_tamanhoAdd'),
    path('saboresUp/<int:pk>/', views.sabores_up, name='url_saborNovo'),
    path('delete/<int:pk>/', views.sabores_del, name='url_delete'),
]