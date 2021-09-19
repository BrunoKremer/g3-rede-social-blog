from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ( 'comentario', 'interacao')
        labels = { 'comentario': 'Comentário', 'interacao':'O que achou deste artigo?'}