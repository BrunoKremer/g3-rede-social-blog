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
    
    # URL PRINCIPAL DA LOJA
    path('', views.filter_categoria , name = 'categoria'),
    path('', views.home , name = 'home'),
    

]