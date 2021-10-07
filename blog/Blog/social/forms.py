
from django import forms
from .models import Comment, Publicacao


# Formulário de publicação, onde é solicitado o conteúdo e caso o usuário queira, uma foto
class Publicacao_form(forms.ModelForm):

    class Meta:
        model = Publicacao

        widgets = {
            'conteudo': forms.Textarea(attrs={'placeholder': 'Escreva algo', 'id': 'editor'}),
        }
        fields = ('conteudo', 'foto')
        labels = {'conteudo': '', 'foto': ''}

# Form de comentário na publicação
class Comentario_publi(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'comentario'}
        # widgets = {
        #     'comentario': forms.Textarea(attrs={'placeholder': 'Faça um comentário..'}),
        # }
        labels = {'comentario':'comentario'}

        
