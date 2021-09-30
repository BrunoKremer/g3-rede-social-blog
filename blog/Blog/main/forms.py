from django import forms
from .models import Comentarios

# Formulário de comentários no blog

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ( 'comentario', )
        labels = { 'comentario': 'Comentário'}