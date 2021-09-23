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
    path('feed', views.feed, name='feed'),  
    path('deletar-post/<str:id>/', views.deletarPublicacao, name='deletar-post'),
    path('editar-post/<str:id>/', views.editarPublicacao, name='editar-post'),
    
]

