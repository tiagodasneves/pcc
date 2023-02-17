from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.PositiveSmallIntegerField(default=0)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)

    class meta:
        abstract = True

    def _str_(self):
        return self.name

class Pessoa(User):
    cpf = models.CharField(max_length=11, primary_key=True)
    genderChoice = (("M", 'Masculino'), ("F", 'Feminino'), ("O", 'Outro'))
    gender = models.CharField(max_length = 1, choices = genderChoice, default = "O")

class Instituicao(User):
    cnpj = models.CharField(max_length=14, primary_key=True)
    pessoa = models.ManyToManyField(Pessoa, related_name="Cabelo", through="Cabelo")
    pessoa1 = models.ManyToManyField(Pessoa, related_name="Solicitacao", through="Solicitacao")

class Peruca(models.Model):
    instituicao = models.ForeignKey("Instituicao", on_delete=models.CASCADE, related_name='perucas')
    cor = models.CharField(max_length= 50)
    tamanhoEscolha = (("C", "Curto"), ("M", "Médio"), ("G", "Grande"))
    tamanho = models.CharField(max_length = 1, choices = tamanhoEscolha, default = "M")
    ImagemPeruca = models.ImageField(upload_to='ImageFiles', null=True, blank=True)

class Solicitacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    peruca = models.OneToOneField(Peruca, on_delete=models.SET_NULL, null=True)
    codigoRastreio = models.CharField(max_length=13, null=True, blank=True)
    situacaoEscolha = (("A", "Aprovada"), ("N", "Não aprovada"))
    situacao = models.CharField(max_length=1, choices=situacaoEscolha, default="N")

class Cabelo(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    comprimento = models.PositiveSmallIntegerField()
    cor = models.CharField(max_length=50)
    tipoEscolha = (("L", "Liso"), ("O", "Ondulado"), ("C", "Cacheado"))
    tipo = models.CharField(max_length=1, choices = tipoEscolha, default = "L")
    codigoRastreio = models.CharField(max_length=13, null=True, blank=True)