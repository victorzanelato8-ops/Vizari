from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CadastroClienteForm
from .models import Cliente

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/index.html', {'clientes': clientes})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            usuario, cliente = form.save()
            login(request, usuario)  # já loga o cliente automaticamente após cadastrar
            return redirect('cardapio')
    else:
        form = CadastroClienteForm()

    return render(request, 'clientes/cadastro.html', {'form': form})