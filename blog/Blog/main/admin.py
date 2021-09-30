from django.contrib import admin
from .models import Curtir, Post, Categoria, Indicacao, Comentarios

# Aqui estamos fazendo o registro de nossas tabelas no ADMIN do Django

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Indicacao)
admin.site.register(Comentarios)
admin.site.register(Curtir)
