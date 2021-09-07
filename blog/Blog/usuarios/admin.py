from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import UsuarioFormChange, UsuarioForm
from .models import CustomUser

admin.site.register(CustomUser)

def _autor(self, instance):
    return f'{instance.user.get_full_name()}'



# # Register your models here.
# @admin.register(Usuarios)
# class CustomUsuarioAdmin(UserAdmin):
#     add_form = UsuarioForm
#     form = UsuarioFormChange
#     model = Usuarios
#     list_display = ('first_name', 'last_name', 'email', 'telefone', 'aniversario','endereco', 'ocupacao', 'linguagens')
#     fieldsets = (
#         (None, {'fields':('email', 'password')}),
#         ('Informações Pessoais', {'fields':('first_name', 'last_name','telefone', 'aniversario','endereco', 'ocupacao', 'linguagens')}),
#         ('Permissões', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Datas Importantes', {'fields':('last_login','date_joined')}),
#     )