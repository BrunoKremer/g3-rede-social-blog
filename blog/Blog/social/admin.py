from django.contrib import admin
from .models import Like, Publicacao, Comentario


# Registrando os models de Publicacao e comentarios na rede social
admin.site.register(Publicacao)
admin.site.register(Comentario)
admin.site.register(Like)
