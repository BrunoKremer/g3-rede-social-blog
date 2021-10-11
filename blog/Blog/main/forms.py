from django import forms
from .models import Comentarios, Reviews

# Formulário de comentários no blog

class ComentariosForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ( 'comentario', )
        labels = { 'comentario': 'Comentário'}