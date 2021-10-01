from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'social'

urlpatterns = [
    # Url do Feed, onde mostra todas publicações feitas
    path('feed', views.feed, name='feed'), 
    # Url para deletar POST escolhido pelo usuário, utilizamos a ID para fazer a seleção do POST
    path('deletar-post/<str:id>/', views.deletarPublicacao, name='deletar-post'),
    # Url para editar POST escolhido pelo usuário
    path('editar-post/<str:id>/', views.editarPublicacao, name='editar-post'),
    # Url para comentar POST escolhido pelo usuário
    path('comentar_post/<str:id>/', views.comentar_Publicacao, name='comentar_post'),

    path('like/', views.like_post, name='like_post'),
    
]

