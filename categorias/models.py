from django.db import models
from decimal import Decimal

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.categoria


class Produto(models.Model):
    produto = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2,default=Decimal("0.00"))
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto
