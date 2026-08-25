from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.index, name='clientes'),
    path('clientes/cadastro/', views.cadastro, name='cadastro'),
]
