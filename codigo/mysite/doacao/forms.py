from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pessoa

class PessoaForm(ModelForm):
    
    class Meta:
        model = Pessoa
        fields = "__all__"