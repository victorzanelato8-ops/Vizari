from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from categorias.models import Produto
from .carrinho import Carrinho
from .models import Pedido, ItemPedido

def adicionar_ao_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.adicionar(produto_id)
    messages.success(request, f'{produto.nome} adicionado ao pedido!')
    return redirect('cardapio')

def remover_do_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    carrinho.remover(produto_id)
    return redirect('ver_carrinho')

def atualizar_carrinho(request, produto_id):
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))
        carrinho = Carrinho(request)
        carrinho.atualizar_quantidade(produto_id, quantidade)
    return redirect('ver_carrinho')

def ver_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'pedidos/carrinho.html', {'carrinho': carrinho})

@login_required(login_url='login')
def finalizar_pedido(request):
    carrinho = Carrinho(request)

    if carrinho.total_itens() == 0:
        messages.warning(request, 'Seu carrinho está vazio.')
        return redirect('ver_carrinho')

    if request.method == 'POST':
        mesa = request.POST.get('mesa')
        if not mesa:
            messages.error(request, 'Selecione o número da mesa.')
            return render(request, 'pedidos/finalizar.html', {'carrinho': carrinho})

        pedido = Pedido.objects.create(usuario=request.user, mesa=mesa)
        for item in carrinho:
            ItemPedido.objects.create(
                pedido=pedido,
                produto=item['produto'],
                quantidade=item['quantidade'],
                preco_unitario=item['produto'].preco
            )

        carrinho.limpar()
        messages.success(request, f'Pedido #{pedido.id} confirmado para a Mesa {mesa}!')
        return redirect('pedido_confirmado', pedido_id=pedido.id)

    return render(request, 'pedidos/finalizar.html', {
        'carrinho': carrinho,
        'mesas': range(1, 28),
    })

@login_required(login_url='login')
def pedido_confirmado(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
    return render(request, 'pedidos/confirmado.html', {'pedido': pedido})

def eh_staff(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(eh_staff, login_url='login')
def painel_pedidos(request):
    pedidos = Pedido.objects.select_related('usuario').prefetch_related('itens__produto').all()
    return render(request, 'pedidos/painel.html', {'pedidos': pedidos})
