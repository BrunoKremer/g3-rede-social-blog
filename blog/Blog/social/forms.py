
from django import forms
from .models import Publicacao,Comentario

# Formulário de publicação, onde é solicitado o conteúdo e caso o usuário queira, uma foto
class Publicacao_form(forms.ModelForm):

    class Meta:
        model = Publicacao

        widgets = {
            'conteudo': forms.Textarea(attrs={'placeholder': 'Escreva algo'}),
        }
        fields = ('conteudo', 'foto')
        labels = {'conteudo': ''}

# Form de comentário na publicação
class Comentario_publi(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = {'comentario', 'foto'}
        # widgets = {
        #     'comentario': forms.Textarea(attrs={'placeholder': 'Faça um comentário..'}),
        # }
        labels = {'comentario': '', 'foto': ''}

        
