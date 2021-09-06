# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .models import Usuarios

# class UsuarioForm(UserCreationForm):

#     class Meta:
#         model = Usuarios
#         fields = ('first_name', 'last_name', 'telefone', 'aniversario','endereco', 'ocupacao', 'linguagens')
#         labels = {'username': 'Username/E-mail'}

#     def save(self, commit: True):
#         user =  super().save(commit=False)
#         user.set_password(self.cleaned_data["passoword1"])
#         user.email = self.cleaned_data["username"]
#         if commit:
#             user.save()
#         return user


# class UsuarioFormChange(UserChangeForm):

#     class Meta:
#         model = Usuarios
#         fields = ('first_name', 'last_name', 'telefone', 'aniversario','endereco', 'ocupacao', 'linguagens')
    