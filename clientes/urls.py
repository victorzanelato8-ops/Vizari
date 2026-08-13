from django.urls import path
from . import views

urlpatterns = [    path('clientes/', views.clientes, name='clientes'),    path('clientes/cadastro/', views.cadastro, name='cadastro'),
    # suas outras rotas que jÃ¡ existem continuam aqui
]
