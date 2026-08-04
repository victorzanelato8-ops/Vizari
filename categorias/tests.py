from django.test import TestCase
from .models import Categoria, Produto

class CategoriaModelTest(TestCase):
    def test_criar_categoria(self):
        categoria = Categoria.objects.create(nome="Massas")
        self.assertEqual(categoria.nome, "Massas")
        self.assertEqual(str(categoria), "Massas")  # testa o __str__

class ProdutoModelTest(TestCase):
    def setUp(self):
        # roda antes de cada teste dessa classe
        self.categoria = Categoria.objects.create(nome="Pizzas")

    def test_criar_produto(self):
        produto = Produto.objects.create(
            nome="Pizza Margherita",
            categoria=self.categoria,
            preco=45.90,
            disponivel=True
        )
        self.assertEqual(produto.nome, "Pizza Margherita")
        self.assertEqual(produto.categoria, self.categoria)
        self.assertTrue(produto.disponivel)

    def test_produto_relacionado_a_categoria(self):
        Produto.objects.create(nome="Pizza Calabresa", categoria=self.categoria, preco=42.00)
        Produto.objects.create(nome="Pizza Portuguesa", categoria=self.categoria, preco=44.00)
        # testa se o related_name 'produtos' funciona
        self.assertEqual(self.categoria.produtos.count(), 2)