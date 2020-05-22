from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('pedidos/', views.pedir_view, name='url_pedidos'),
]

