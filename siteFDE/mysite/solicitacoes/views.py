from django.shortcuts import render, redirect, get_object_or_404
from .models import Peruca

def cadastrar_peruca(request):
    if request.method == 'POST':
        tamanho = request.POST['tamanho']
        tipo = request.POST['tipo']
        cor = request.POST['cor']
        foto = request.FILES['foto']
        
        peruca = Peruca(tamanho=tamanho, tipo=tipo, cor=cor, foto=foto, selecionada=False)
        peruca.save()
        
        return redirect('listar_perucas')
    
    return render(request, 'solicitacoes/perucas.html')
    
def listar_perucas(request):
    perucas = Peruca.objects.all()
    context = {'perucas': perucas}
    return render(request, 'solicitacoes/perucas.html', context)

def editar_peruca(request, pk):
    peruca = get_object_or_404(Peruca, pk=pk)
    
    if request.method == 'POST':
        peruca.tamanho = request.POST['tamanho']
        peruca.tipo = request.POST['tipo']
        peruca.cor = request.POST['cor']
        peruca.foto = request.FILES.get('foto')
        peruca.save()
        return redirect('listar_perucas')
    
    context = {'peruca': peruca}
    return render(request, 'solicitacoes/editar_peruca.html', context)

def excluir_peruca(request, pk):
    peruca = get_object_or_404(Peruca, pk=pk)
    
    if request.method == 'POST':
        peruca.delete()
        return redirect('listar_perucas')
    
    context = {'peruca': peruca}
    return render(request, 'solicitacoes/perucas.html', context)
