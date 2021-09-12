from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ('usuario', 'comentario', 'email', 'interacao')
        labels = {'usuario': 'Usuário', 'comentario': 'Comentário', 'interacao':'O que achou deste artigo?'}