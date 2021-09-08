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
    path('cadastro', views.CadastroFormView.as_view(), name='cadastro'),
    path('cadastro/sucess', views.RegistradoView.as_view(), name='sucess'),
    path('profile/<int:pk>', views.ProfileView, name='profile'),

    
]