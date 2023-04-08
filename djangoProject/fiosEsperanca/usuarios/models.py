from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.rua}, {self.bairro}, {self.cidade} - {self.estado}'

class Pessoa(AbstractBaseUser):
    # Campos personalizados da classe Pessoa
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    enderecos = models.ManyToManyField(Endereco)

    # Campos padrão da classe User
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome

    def add_endereco(self, endereco):
        self.enderecos.add(endereco)

    def remove_endereco(self, endereco):
        self.enderecos.remove(endereco)


class Instituicao(AbstractBaseUser):
    # Campos personalizados da classe Pessoa
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    enderecos = models.ManyToManyField(Endereco)

    # Campos padrão da classe User
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome

    def add_endereco(self, endereco):
        self.enderecos.add(endereco)

    def remove_endereco(self, endereco):
        self.enderecos.remove(endereco)