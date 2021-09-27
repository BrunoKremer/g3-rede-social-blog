
from django import forms
from .models import Publicacao,Comentario

class Publicacao_form(forms.ModelForm):

    class Meta:
        model = Publicacao

        widgets = {
            'conteudo': forms.Textarea(attrs={'placeholder': 'Escreva algo'}),
        }
        fields = ('conteudo', 'foto')
        labels = {'conteudo': ''}

class Comentario_publi(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = {'comentario', 'foto'}
        # widgets = {
        #     'comentario': forms.Textarea(attrs={'placeholder': 'Faça um comentário..'}),
        # }
        labels = {'comentario': '', 'foto': ''}

        
