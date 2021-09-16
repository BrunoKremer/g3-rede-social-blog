from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioFormChange, UsuarioForm
from .models import CustomUser

def _autor(self, instance):
    return f'{instance.user.get_full_name()}'

@admin.register(CustomUser)
class CustomUsuarioAdmin(UserAdmin):
    add_form = UsuarioForm
    form = UsuarioFormChange
    model = CustomUser
    list_display = ('first_name', 'last_name', 'email', 'telefone', 'ocupacao')
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        ('Informações Pessoais', {'fields':('first_name', 'last_name','telefone', 'ocupacao', 'genero','cidade', 'estado', 'CEP', 'foto')}),
        ('Links', {'fields':('link_fb', 'link_tt', 'link_ig', 'link_git')}),
        ('Permissões', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields':('last_login','date_joined')}),
    )