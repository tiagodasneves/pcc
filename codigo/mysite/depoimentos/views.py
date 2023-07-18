from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Depoimento

def home(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'core/index.html', {'depoimentos': depoimentos})

def depoimentos(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'core/index.html', {'depoimentos': depoimentos})

@login_required
def criar_depoimento(request):
    if request.method =='POST':
        conteudo = request.POST.get('conteudo')
        autor = request.user
        depoimento = Depoimento(conteudo=conteudo, autor=autor)
        depoimento.save()
        return redirect (home)
    else:
        return render(request, 'core/index.html')

@login_required
def deletar_depoimento(request, depoimento_id):
    depoimento = get_object_or_404(Depoimento, id=depoimento_id)
    if depoimento.autor == request.user:
        depoimento.delete()
        return redirect(home)
    else:
        return redirect(home)
    
@login_required
def editar_depoimento(request, id):
    depoimento = Depoimento.objects.get(id=id)
    if request.user == depoimento.autor:
        if request.method == 'POST':
            conteudo = request.POST.get('conteudo')
            depoimento.conteudo = conteudo
            depoimento.save()
            return redirect(home)
        else:
            return render(request, 'core/index.html', {'depoimento': depoimento, 'user': request.user})
    else:
        return redirect(home)

