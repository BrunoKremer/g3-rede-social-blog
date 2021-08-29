from django.contrib import admin
from .models import Post, Categoria, Indicacao, Comentarios

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Indicacao)
admin.site.register(Comentarios)

# Register your models here.
