from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from django.urls import reverse

def cadastro(request):
    if request.method == 'POST':
        #try:
            #usuario_email = request.POST.get('email')
            #usuario_username = request.POST.get('username')

            #if usuario_email or usuario_username:
                #return render(request, 'core/cadastro.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail ou mesmo username'})
            
        #except User.DoesNotExist:
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

            return render(request, 'usuarios/login.html')

    else:
        return render (request, 'usuarios/cadastro.html')

def user_login (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect(reverse('main:home'))
        else:
            return render(request, 'usuarios/login.html', {'msg': 'Credenciais inválidas!'})

    else:
        return render(request, 'usuarios/login.html')
    
@login_required
def sair(request):
    logout(request)
    return redirect(reverse('main:home'))

def ler_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'core/ler_usuarios.html', {"usuarios": usuarios})

def editar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'core/editar_usuario.html', {"usuario": usuario})

def atualizar_usuario(request, id):
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

def deletar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(ler_usuarios)

def editar_perfil(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'core/editar_perfil.html', {"usuario": usuario})

def atualizar_perfil(request, id):
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

    return redirect(reverse('main:home'))
