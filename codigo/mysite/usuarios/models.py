from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    nome=models.CharField(max_length=200, null=True)
    sobrenome=models.CharField(max_length=200, null=True)
    telefone=models.CharField(max_length=16, null=True)
    rua = models.CharField(max_length=100, null=True)
    numero=models.IntegerField(null=True)
    bairro=models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')

