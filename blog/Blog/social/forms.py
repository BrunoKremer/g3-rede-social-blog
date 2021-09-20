
from django import forms
from .models import Publicacao

class Publicacao_form(forms.ModelForm):

    class Meta:
        model = Publicacao

        widgets = {
            'conteudo': forms.Textarea(attrs={'placeholder': 'Escreva algo'}),
        }
        fields = ('conteudo', 'foto')
        labels = {'conteudo': ''}


        
