from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Depoimento


def depoimentos(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'depoimentos/depoimentos.html', {'depoimentos': depoimentos})

@login_required
def criar_depoimento(request):
    if request.method =='POST':
        conteudo = request.POST.get('conteudo')
        autor = request.user
        depoimento = Depoimento(conteudo=conteudo, autor=autor)
        depoimento.save()
        return redirect (depoimentos)
    else:
        return render(request, 'depoimentos/criar_depoimento.html')

@login_required
def deletar_depoimento(request, depoimento_id):
    depoimento = get_object_or_404(Depoimento, id=depoimento_id)

    if depoimento.autor == request.user:
        depoimento.delete()
        return redirect(depoimentos)
    else:
        return redirect(depoimentos)
