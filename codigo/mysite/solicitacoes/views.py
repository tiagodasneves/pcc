from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Peruca, SolicitacaoPeruca

@login_required
def cadastrar_peruca(request):
    if request.user.is_staff:
        if request.method == 'POST':
            tamanho = request.POST.get('tamanho')
            tipo = request.POST.get('tipo')
            cor = request.POST.get('cor')
            foto = request.FILES.get('foto')
            peruca = Peruca(tamanho=tamanho, 
                            tipo=tipo, 
                            cor=cor, 
                            foto=foto, 
                            selecionada=False)
            peruca.save()
            return redirect('listar_perucas')
        else:
            return redirect('listar_perucas')
    else:
        return redirect('minhas_solicitacoes')

@login_required
def listar_perucas(request):
    if request.user.is_staff:
        perucas_disponiveis = Peruca.objects.filter(selecionada=False)
        context = {'perucas_disponiveis': perucas_disponiveis}
        return render(request, 'solicitacoes/perucas.html', context)
    else:
        return redirect('minhas_solicitacoes')

@login_required
def editar_peruca(request, id):
    if request.user.is_staff:
        peruca = get_object_or_404(Peruca, id=id)
        if request.method == 'POST':
            peruca.tamanho = request.POST.get('tamanho')
            peruca.tipo = request.POST.get('tipo')
            peruca.cor = request.POST.get('cor')
            peruca.save()
            return redirect('listar_perucas')
        else:
            context = {'peruca': peruca}
            return render(request, 'solicitacoes/editar_peruca.html', context)
    else:
        return redirect('minhas_solicitacoes')

@login_required
def deletar_peruca(request, id):
    if request.user.is_staff:
        peruca = get_object_or_404(Peruca, id=id)
        if request.method == 'POST':
            peruca.delete()
            return redirect('listar_perucas')
    else:
        return redirect('minhas_solicitacoes')

@login_required
def fazer_solicitacao(request):
    if request.method == 'POST':
        solicitacao = SolicitacaoPeruca()
        solicitacao.peruca_id = request.POST.get('peruca')
        solicitacao.usuario_id = request.user.id
        solicitacao.questao1 = request.POST.get('questao1')
        solicitacao.questao2 = request.POST.get('questao2')
        solicitacao.questao3 = request.POST.get('questao3')
        solicitacao.comprovante = request.FILES.get('comprovante')
        solicitacao.status = 'analise'
        solicitacao.save()
        peruca_id = request.POST.get('peruca')
        peruca = Peruca.objects.get(id=peruca_id)
        peruca.selecionada = True
        peruca.save()
        return redirect('listar_perucas')
    else:
        perucas_disponiveis = Peruca.objects.filter(selecionada=False)
        context = {'perucas_disponiveis': perucas_disponiveis}
        return render(request, 'solicitacoes/fazer_solicitacao.html', context)
    
@login_required
def listar_solicitacoes(request):
    if request.user.is_staff:
        solicitacoes = SolicitacaoPeruca.objects.all()
        context = {'solicitacoes': solicitacoes}
        return render(request, 'solicitacoes/listar_solicitacoes.html', context)
    else:
        return redirect('minhas_solicitacoes')

@login_required
def detalhes_solicitacao(request, id):
        solicitacao = get_object_or_404(SolicitacaoPeruca, id=id)
        context = {'solicitacao': solicitacao}
        return render(request, 'solicitacoes/detalhes_solicitacao.html', context)

@login_required
def aprovar_solicitacao(request, id):
    if request.user.is_staff:
        solicitacao = get_object_or_404(SolicitacaoPeruca, id=id)
        solicitacao.status = 'aprovado'
        solicitacao.save()
        return redirect('listar_solicitacoes')
    else:
        return redirect('minhas_solicitacoes')

@login_required
def rejeitar_solicitacao(request, id):
    if request.user.is_staff:
        solicitacao = get_object_or_404(SolicitacaoPeruca, id=id)
        motivo_rejeicao = request.POST.get('motivo')
        solicitacao.motivo_rejeicao = motivo_rejeicao
        solicitacao.status = 'rejeitado'
        solicitacao.peruca.selecionada = False
        solicitacao.peruca.save()
        solicitacao.peruca = None
        solicitacao.save()
        return redirect('listar_solicitacoes')
    else:
        return redirect('minhas_solicitacoes')

@login_required
def addCR(request, id):
    if request.user.is_staff:
            solicitacao = get_object_or_404(SolicitacaoPeruca, id=id)
            solicitacao.status = 'caminho'
            solicitacao.codRastreio = request.POST.get('codRastreio')
            solicitacao.save()
            return redirect('listar_solicitacoes')
    else:
        return redirect('minhas_solicitacoes')

@login_required
def minhas_solicitacoes(request):
    solicitacoes = SolicitacaoPeruca.objects.filter(usuario=request.user)
    return render(request, 'solicitacoes/minhas_solicitacoes.html', {'solicitacoes': solicitacoes})

@login_required
def finalizar_entrega(request, id):
    solicitacao = get_object_or_404(SolicitacaoPeruca, id=id)
    solicitacao.status = 'entregue'
    solicitacao.save()
    return redirect('minhas_solicitacoes')

@login_required
def deletar_solicitacao(request, id):
    solicitacao = get_object_or_404(SolicitacaoPeruca, id=id)
    if request.user == solicitacao.usuario or request.user.is_superuser:
        solicitacao.delete()
        return redirect('listar_solicitacoes')
    else:
        return redirect('minhas_solicitacoes')

