from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='clientes'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
