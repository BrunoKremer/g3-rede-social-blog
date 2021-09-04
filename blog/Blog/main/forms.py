from django import forms
from .models import Comentarios

class FormComentario(forms.Form):
    comentario = forms.CharField(widget= forms.Textarea())