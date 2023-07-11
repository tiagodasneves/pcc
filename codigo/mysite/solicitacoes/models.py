from django.db import models
from usuarios.models import Usuario

class Peruca(models.Model):
    tamanhoEscolhas = (
        ('curto', 'Peruca de tamanho curto'),
        ('medio', 'Peruca de tamanho médio'),
        ('longo', 'Peruca de tamanho longo'),
    )
    tipoEscolhas = (
        ('liso', 'Peruca de cabelo liso'),
        ('ondulado', 'Peruca de cabelo ondulado'),
        ('cacheado', 'Peruca de cabelo cacheado'),
        ('crespo', 'Peruca de cabelo crespo'),
    )
    corEscolhas = (
        ('loiro', 'Peruca de cabelo loiro'),
        ('ruivo', 'Peruca de cabelo ruivo'),
        ('preto', 'Peruca de cabelo preto'),
        ('castanho', 'Peruca de cabelo castanho'),
        ('grisalho', 'Peruca de cabelo grisalho'),
    )
    tamanho = models.CharField(max_length=50, choices=tamanhoEscolhas, null=True, blank=False)
    tipo = models.CharField(max_length=50, choices=tipoEscolhas, null=True, blank=False)
    cor = models.CharField(max_length=50, choices=corEscolhas, null=True, blank=False)
    foto = models.ImageField(upload_to='imagens/perucas', null=True, blank=False)
    selecionada = models.BooleanField(null=True)

class SolicitacaoPeruca(models.Model):
    statusOptions = (
        ('analise', 'Em análise'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('caminho', 'A caminho'),
        ('entregue', 'Entregue'),
    )
    codRastreio = models.CharField(max_length=20, null=True, blank=True)
    peruca = models.OneToOneField(Peruca, on_delete=models.PROTECT, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    questao1 = models.TextField(null=True, blank=False)
    questao2 = models.TextField(null=True, blank=False)
    questao3 = models.TextField(null=True, blank=False)
    comprovante = models.ImageField(upload_to='imagens/comprovantes', null=True, blank=False)
    status = models.CharField(max_length=50, choices=statusOptions)

