from ckeditor.fields import RichTextField
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.categoria


class Post(models.Model):
    categoria = models.ManyToManyField(Categoria)
    titulo = models.CharField(max_length=1000)
    subtitulo = models.CharField(max_length=1000,null=True)
    conteúdo = models.TextField()
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    criado_em = models.DateField(auto_now_add= False)
    foto = models.ImageField(null=True, blank=True, upload_to="static/img/")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-criado_em']


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
    link = models.CharField(max_length=2000,null=True,blank=True)
    criado_em = models.DateField(auto_now_add= False)
    foto = models.FileField(null=True, blank=True, upload_to="static/img/")

    class Meta:
        verbose_name = 'Indicação'
        verbose_name_plural = 'Indicações'

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    posts = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comentarios')
    comentario = models.TextField()

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.comentario
