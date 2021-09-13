"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from main.api import viewsets

router = routers.DefaultRouter()
router.register(r'blog', viewsets.PostViewSet)
router.register(r'category', viewsets.CategoriaViewSet)
router.register(r'indicacao', viewsets.IndicacaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('', include('main.urls', namespace = 'main')),
    path('user/', include('usuarios.urls', namespace = 'usuarios')),
    path('social/', include('social.urls', namespace = 'social')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


admin.site.site_header = 'Infocode'
admin.site.site_title = 'Mantenha-se conectado com todas tecnologias'
admin.site.site_header = 'Sistema de gerenciamento da infocode'
