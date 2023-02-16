from django.contrib import admin
from .models import Pessoa, Instituicao, Peruca,Solicitacao, Cabelo
admin.site.register(Pessoa)
admin.site.register(Instituicao)
admin.site.register(Peruca)
admin.site.register(Solicitacao)
admin.site.register(Cabelo)

# Register your models here.
