from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('emial')
        senha = request.POST.get('senha')
        

        user = User.objects.filter(username=username).first()

        #if (user):
            #return HttpResponse("Já existe um usuário com esse username")
        #else:
            #return HttpResponse("Cadastrado(a) com sucesso!")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        return render(request, 'home_view.html')

def home_view(request):
    return render(request, 'home_view.html')