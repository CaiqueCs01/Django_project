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
]