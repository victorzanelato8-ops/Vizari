from django.shortcuts import render
from .models import Categoria, Produto

def home(request):
    categorias = Categoria.objects.all()
    produtos = Produto.objects.all()
    return render(request,'categoria/index.html', {'categorias': categorias, 'produtos': produtos})



