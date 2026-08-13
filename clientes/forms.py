from django import forms
from django.contrib.auth.models import User
from .models import Cliente

class CadastroClienteForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=150)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    nome = forms.CharField(label='Nome completo', max_length=100)
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone', max_length=20)
    endereco = forms.CharField(label='Endereço', widget=forms.Textarea)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Esse nome de usuário já está em uso.')
        return username

    def save(self):
        dados = self.cleaned_data
        usuario = User.objects.create_user(
            username=dados['username'],
            password=dados['password'],
            email=dados['email']
        )
        cliente = Cliente.objects.create(
            usuario=usuario,
            nome=dados['nome'],
            email=dados['email'],
            telefone=dados['telefone'],
            endereco=dados['endereco']
        )
        return usuario, cliente