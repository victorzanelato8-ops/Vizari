from categorias.models import Produto

class Carrinho:
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get('carrinho')
        if not carrinho:
            carrinho = self.session['carrinho'] = {}
        self.carrinho = carrinho

    def adicionar(self, produto_id, quantidade=1):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            self.carrinho[produto_id]['quantidade'] += quantidade
        else:
            self.carrinho[produto_id] = {'quantidade': quantidade}
        self.salvar()

    def remover(self, produto_id):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()

    def atualizar_quantidade(self, produto_id, quantidade):
        produto_id = str(produto_id)
        if produto_id in self.carrinho:
            if quantidade <= 0:
                self.remover(produto_id)
            else:
                self.carrinho[produto_id]['quantidade'] = quantidade
                self.salvar()

    def limpar(self):
        self.session['carrinho'] = {}
        self.salvar()

    def salvar(self):
        self.session.modified = True

    def __iter__(self):
        produto_ids = self.carrinho.keys()
        produtos = Produto.objects.filter(id__in=produto_ids)
        for produto in produtos:
            item = self.carrinho[str(produto.id)]
            yield {
                'produto': produto,
                'quantidade': item['quantidade'],
                'subtotal': produto.preco * item['quantidade'],
            }

    def total(self):
        return sum(item['subtotal'] for item in self)

    def total_itens(self):
        return sum(item['quantidade'] for item in self.carrinho.values())