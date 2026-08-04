from django.urls import path
from clientes import views

urlpatterns = [    
    path('clientes', views.clientes_view, name='clientes'),    
]