from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastrar_pessoa.html', {'form': form})

def editar_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('lista_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'editar_pessoa.html', {'form': form})

def excluir_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    pessoa.delete()
    return redirect('lista_pessoas')
