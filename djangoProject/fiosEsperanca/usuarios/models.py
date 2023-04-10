from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Pessoa(AbstractBaseUser):
    # Campos personalizados da classe Pessoa
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)

    # Campos padrão da classe User
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    rua = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255, null=True)
    cidade = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=2, null=True)
    escolhaRegiao = [
        ('NO', 'Norte'),
        ('NE', 'Nordeste'),
        ('SE', 'Sudeste'),
        ('CO', 'Centro-Oeste'),
        ('SU', 'Sul'),
    ]
    regiao = models.CharField(max_length=2, choices=escolhaRegiao, default='NO')

    def __str__(self):
        return self.nome


class Instituicao(AbstractBaseUser):
    # Campos personalizados da classe Instituição
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)

    # Campos padrão da classe User
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # Endereço
    rua = models.CharField(max_length=255, null=True)
    bairro = models.CharField(max_length=255, null=True)
    cidade = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=2, null=True)
    escolhaRegiao = [
        ('NO', 'Norte'),
        ('NE', 'Nordeste'),
        ('SE', 'Sudeste'),
        ('CO', 'Centro-Oeste'),
        ('SU', 'Sul'),
    ]
    regiao = models.CharField(max_length=2, choices=escolhaRegiao, default='NO')

    def __str__(self):
        return self.nome

    @classmethod
    def listar_por_regiao(cls):
        ordem_regioes = ['NO', 'NE', 'SE', 'CO', 'SU']
        return cls.objects.order_by(ordem_regioes.index('regiao'))
