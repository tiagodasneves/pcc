from django.db import models
from usuarios.models import Usuario

class Depoimento(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    conteudo = models.TextField(blank=False)
