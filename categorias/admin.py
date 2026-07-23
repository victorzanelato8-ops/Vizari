from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'preco', 'categoria']
