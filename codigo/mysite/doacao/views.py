from django.shortcuts import render, redirect
from .models import Question, Doacao
from .forms import DoacaoForm

def quest(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados do formulário no banco de dados
            return redirect('result')
    else:
        form = DoacaoForm()
    return render(request, 'solicitacao.html', {'form': form})

def resultados(request):
    questionarios = Doacao.objects.all()
    return render(request, 'resultados.html', {'resultados': resultados})

def home(request):
    return render(request, 'home.html')


def result(request):
    questions = Question.objects.all()
    return render(request, 'result.html', {'questions': questions})

