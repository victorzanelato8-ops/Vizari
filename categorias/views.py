from django.shortcuts import render
from .models import Categoria

def cardapio(request):
    categorias = Categoria.objects.prefetch_related('produtos').all()
    return render(request, 'categorias/cardapio.html', {'categorias': categorias})
