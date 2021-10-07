from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey
from usuarios.models import CustomUser

import uuid

# Modelo de Publicação
# Estamos importando o Custom User para autenticar o usuário
class Publicacao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add= True)
    foto = models.ImageField(null = True, blank = True,  upload_to="static/img/")
    liked = models.ManyToManyField(User,default=None,blank=True,related_name='LIked')
    
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.usuario.first_name

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('l','Like'),
    ('d','Deslike'),
)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Publicacao,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)


class Comment(models.Model):
    usuario = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    publicacao = models.ForeignKey(Publicacao,on_delete=models.CASCADE)
    comentario = models.TextField(null=True,blank=True)
    criacao = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.comentario


