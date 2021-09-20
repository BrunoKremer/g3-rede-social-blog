from django.contrib.auth.models import User
from django.db import models
from usuarios.models import CustomUser


class Publicacao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add= True)
    foto = models.FileField(null = True, blank = True,  upload_to="static/img/")
    
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.usuario.first_name