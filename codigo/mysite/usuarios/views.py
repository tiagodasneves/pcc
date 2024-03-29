from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from depoimentos.models import Depoimento

def home(request):
    depoimentos = Depoimento.objects.all()
    context = {'depoimentos': depoimentos}
    return render(request, 'core/index.html', context)

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if Usuario.objects.filter(username=username).exists():
            return render(request, 'usuarios/cadastro.html', {'msg_username': 'Este username já está em uso!'})
        
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'usuarios/cadastro.html', {'msg_email': 'Este email já está cadastrado!'})
        
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            return render(request, 'usuarios/cadastro.html', {'msg_password': 'As senhas não são iguais!'})


        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')

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
                                                  estado=estado,
                                                  cep = cep)
        novoUsuario.save()

        return render(request, 'usuarios/login.html')

    else:
        return render(request, 'usuarios/cadastro.html')
    
def entrar (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect(home)
        else:
            return render(request, 'usuarios/login.html', {'msg': 'Credenciais inválidas!'})

    else:
        return render(request, 'usuarios/login.html')
    
@login_required
def sair(request):
    logout(request)
    return redirect(home)

@login_required
def ler_usuarios(request):
    if request.user.is_staff:
        usuarios = Usuario.objects.all()
        context = {"usuarios": usuarios}
        return render(request, 'usuarios/ler_usuarios.html', context)
    else:
        return redirect(home)

@login_required
def editar_usuario(request, id):
    if request.user.is_staff:
        if request.method == 'GET':
            usuario = Usuario.objects.get(id=id)
            context = {"usuario": usuario}
            return render(request, 'usuarios/editar_usuario.html', context)
        else:
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            telefone = request.POST.get('telefone')
            rua = request.POST.get('rua')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            cep = request.POST.get('cep')

            usuario = Usuario.objects.get(id=id)
            usuario.nome = nome
            usuario.sobrenome = sobrenome
            usuario.telefone = telefone
            usuario.rua = rua
            usuario.numero = numero 
            usuario.bairro = bairro 
            usuario.cidade = cidade 
            usuario.estado = estado
            usuario.cep = cep
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
        context = {"usuario": usuario}
        return render(request, 'usuarios/editar_perfil.html', context)
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        telefone = request.POST.get('telefone')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')

        usuario = Usuario.objects.get(id=id)
        usuario.nome = nome
        usuario.sobrenome = sobrenome
        usuario.telefone = telefone
        usuario.rua = rua
        usuario.numero = numero 
        usuario.bairro = bairro 
        usuario.cidade = cidade 
        usuario.estado = estado
        usuario.cep = cep
        usuario.save()

        return redirect(home)

