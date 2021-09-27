from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from django import forms

# Formulário para cadastrar usuário

class UsuarioForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'email')
        labels = {'username': 'Usuário'}
# Formulário para editar informações do usuário

class UsuarioFormChange(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telefone', 'estado','cidade', 'ocupacao', 'genero', 'CEP', 'link_fb', 'link_tt', 'link_ig', 'link_git')
        labels = {'link_fb': 'Facebook', 'link_tt':'Twitter', 'link_ig': 'Instagram', 'link_git':'Github'}

        def save(self, commit= True):
            user =  super().save(commit=False)    
            if commit:
                user.save()
            return user