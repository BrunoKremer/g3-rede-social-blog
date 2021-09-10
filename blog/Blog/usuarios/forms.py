from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from django import forms

class UsuarioForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'email', 'telefone')
        labels = {'username': 'Usuário'}

class UsuarioFormChange(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telefone', 'estado','cidade')