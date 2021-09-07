from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

class UsuarioForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'telefone')
        labels = {'username': 'Username/E-mail'}

    # def save(self, commit: True):
    #     user =  super().save(commit=False)
    #     user.set_password(self.cleaned_data["passoword1"])
    #     user.email = self.cleaned_data["username"]
    #     if commit:
    #         user.save()
    #     return user


# class UsuarioFormChange(UserChangeForm):

#     class Meta:
#         model = Usuarios
#         fields = ('first_name', 'last_name', 'telefone', 'aniversario','endereco', 'ocupacao', 'linguagens')
    