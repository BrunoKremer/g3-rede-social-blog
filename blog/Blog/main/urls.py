from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve

from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    # Url principal do blog
    path('', views.home, name = 'post'),
    # Url que redireciona para um artigo especificio pelo ID
    path('<int:pk>/', views.PostDetailView, name='post_detail'),
    # Url que redireciona para nossas indicações de livros e cursos
    path('indicacao/', views.indicacao, name='indicacao'),
    # Url que redireciona para uma indicação especificia pelo ID
    path('indicacao/<int:pk>/', views.IndicacaoDetailView.as_view(), name='indicacao_detail'),
    path('contato', views.Contato_view.as_view(), name='contato'),

    path('curtir/', views.curtir_post, name='curtir_post'),
]