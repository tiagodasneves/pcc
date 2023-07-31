from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Depoimento

def home(request):
    depoimentos = Depoimento.objects.all()
    context = {'depoimentos': depoimentos}
    return render(request, 'core/index.html', context)

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
def deletar_depoimento(request, id):
    depoimento = get_object_or_404(Depoimento, id=id)
    if depoimento.autor == request.user or request.user.is_superuser:
        depoimento.delete()
        return redirect(home)
    else:
        return redirect(home)
