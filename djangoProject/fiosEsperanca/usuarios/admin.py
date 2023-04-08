from django.contrib import admin

from.models import Endereco
from.models import Pessoa
from.models import Instituicao

admin.site.register(Endereco)
admin.site.register(Pessoa)
admin.site.register(Instituicao)

# Register your models here.
