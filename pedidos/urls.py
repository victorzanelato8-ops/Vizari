from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remover/<int:produto_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/atualizar/<int:produto_id>/', views.atualizar_carrinho, name='atualizar_carrinho'),
    path('carrinho/finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
    path('pedido/<int:pedido_id>/confirmado/', views.pedido_confirmado, name='pedido_confirmado'),
    path('painel/pedidos/', views.painel_pedidos, name='painel_pedidos'),
]