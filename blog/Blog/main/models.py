from ckeditor.fields import RichTextField
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria


class Post(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    conteúdo = models.TextField()
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    criado_em = models.DateField(auto_now_add= False)
    foto = models.FileField(null=True, blank=True, upload_to="static/img/")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.titulo

class Indicacao(models.Model):
    INDICACAO_CHOICES = [
        ('l', 'Livro'), ('c', 'Curso')
    ]
    indicacao = models.CharField(max_length=10, choices= INDICACAO_CHOICES, default='curso')
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    autor = models.CharField(max_length=100)
    sinopse = RichTextField()
    criado_em = models.DateField(auto_now_add= False)

    class Meta:
        verbose_name = 'Indicação'
        verbose_name_plural = 'Indicações'

    def __str__(self):
        return self.titulo