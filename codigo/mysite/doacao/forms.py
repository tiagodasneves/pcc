from django import forms
from .models import Doacao

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = ['quest1', 'quest2', 'quest3']