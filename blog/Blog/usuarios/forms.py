from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class UsuarioForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username','first_name', 'last_name', 'email', 'telefone')
        labels = {'username': 'Usuário'}

    # def save(self, commit: True):
    #     user =  super().save(commit=False)
    #     user.first_name = self.cleaned_data["username"]
    #     if commit:
    #         user.save()
    #     return user


# class UsuarioFormChange(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('telefone',)
    