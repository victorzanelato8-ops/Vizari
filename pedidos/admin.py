from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ['produto', 'quantidade', 'preco_unitario']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'mesa', 'status', 'total', 'criado_em']
    list_filter = ['status', 'mesa', 'criado_em']
    list_editable = ['status']
    inlines = [ItemPedidoInline]