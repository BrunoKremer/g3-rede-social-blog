from django.contrib import admin
from .models import Like, Publicacao,Comment


# Registrando os models de Publicacao e comentarios na rede social
admin.site.register(Publicacao)
admin.site.register(Like)
admin.site.register(Comment)
