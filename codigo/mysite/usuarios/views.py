from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from depoimentos.models import Depoimento

def home(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'core/index.html', {'depoimentos': depoimentos})

def cadastro(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            telefone = request.POST.get('telefone')
            password = request.POST.get('password')
            rua = request.POST.get('rua')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')

            novoUsuario = Usuario.objects.create_user(username=username, 
                                                      email=email, 
                                                      nome=nome,
                                                      sobrenome=sobrenome, 
                                                      telefone=telefone, 
                                                      password=password,
                                                      rua=rua,
                                                      numero=numero,
                                                      bairro=bairro,
                                                      cidade=cidade,
                                                      estado=estado)
            novoUsuario.save()

            return render(request, 'usuarios/login2.html')

    else:
        return render (request, 'usuarios/cadastro2.html')

def user_login (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect(home)
        else:
            return render(request, 'usuarios/login2.html', {'msg': 'Credenciais inválidas!'})

    else:
        return render(request, 'usuarios/login2.html')
    
@login_required
def sair(request):
    logout(request)
    return redirect(home)

@login_required
def ler_usuarios(request):
    if request.user.is_staff:
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios/ler_usuarios.html', {"usuarios": usuarios})
    else:
        return redirect(home)

@login_required
def editar_usuario(request, id):
    if request.user.is_staff:
        if request.method == 'GET':
            usuario = Usuario.objects.get(id=id)
            return render(request, 'usuarios/editar_usuario.html', {"usuario": usuario})
        else:
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            telefone = request.POST.get('telefone')
            rua = request.POST.get('rua')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')

            usuario = Usuario.objects.get(id=id)
            usuario.nome = nome
            usuario.sobrenome = sobrenome
            usuario.telefone = telefone
            usuario.rua = rua
            usuario.numero = numero 
            usuario.bairro = bairro 
            usuario.cidade = cidade 
            usuario.estado = estado
            usuario.save()

            return redirect(ler_usuarios)
    else:
        return redirect(home)

@login_required
def deletar_usuario(request, id):
    if request.user.is_staff:
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return redirect(ler_usuarios)
    else:
        return redirect(home)

@login_required
def editar_perfil(request, id):
    if request.method == 'GET':
        usuario = Usuario.objects.get(id=id)
        return render(request, 'usuarios/editar_perfil.html', {"usuario": usuario})
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        usuario = Usuario.objects.get(id=id)
        usuario.nome = nome
        usuario.sobrenome = sobrenome
        usuario.telefone = telefone
        usuario.rua = rua
        usuario.numero = numero 
        usuario.bairro = bairro 
        usuario.cidade = cidade 
        usuario.estado = estado
        usuario.save()

        return redirect(home)

