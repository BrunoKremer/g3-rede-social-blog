from django import forms
from .models import Comentarios

class FormComentario(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields =['comentario']

