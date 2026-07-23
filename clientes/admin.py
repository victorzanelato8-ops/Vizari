from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):  
    list_clientes = ['nome','email','telefone','endereco']
