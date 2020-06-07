from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('profile/<int:pk>/', views.profile, name='url_profile'),
]

