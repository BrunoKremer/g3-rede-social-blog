
from django import forms
from .models import Publicacao

class Publicacao_form(forms.ModelForm):

    class Meta:
        model = Publicacao
        fields = ('usuario','conteudo', 'foto')


        
