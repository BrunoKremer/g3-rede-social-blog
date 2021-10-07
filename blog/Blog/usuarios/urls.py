from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    # View com formulário de cadastro de usuários
    path('cadastro', views.CadastroFormView.as_view(), name='cadastro'),
    # View que redireciona após o sucesso de cadastro
    path('cadastro/sucess', views.RegistradoView.as_view(), name='sucess'),
    # View de perfil do usuário
    path('profile/<int:pk>', views.ProfileView, name='profile'),  
    # View para editar informações de usuários
    path('edit/<int:pk>', views.UserChange.as_view(), name='edit'),

    path('seguir/<int:pk>', views.seguir_usuario, name='seguir'),
]           