from django.shortcuts import render, redirect
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
    
    return render(request, 'solicitacoes/cadastrar_peruca.html')
    
def listar_perucas(request):
    perucas = Peruca.objects.all()
    context = {'perucas': perucas}
    return render(request, 'solicitacoes/listar_perucas.html', context)
