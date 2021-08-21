from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    created_in = models.DateField(auto_now_add= False)
    photo = models.FileField(null=True, blank=True, upload_to="static/img/")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.title

class Indicacao(models.Model):
    INDICACAO_CHOICES = [
        ('livro', 'Livro'), ('curso', 'Curso')
    ]
    indicacao = models.CharField(max_length=10, choices= INDICACAO_CHOICES, default='curso')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    author = models.CharField(max_length=100)
    sinopse = models.TextField()
    created_in = models.DateField(auto_now_add= False)

    def __str__(self):
        return self.title