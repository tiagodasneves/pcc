from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Pessoa

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        pessoa = authenticate(request, email=email, senha=senha)
        if pessoa is not None:
            login(request, pessoa)
            return redirect('pagina_inicial')
        else:
            return render(request, 'login.html', {'erro': 'Credenciais inválidas.'})
    else:
        return render(request, 'login.html')

def pagina_inicial(request):
    return render(request, 'templates/index.html')