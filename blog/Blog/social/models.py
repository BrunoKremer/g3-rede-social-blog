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

# class Comentario(models.Model):
#     usuario=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, related_name='usuario_social')
#     email =models.CharField(max_length=255, null=True)
#     publicacao = models.ForeignKey(Publicacao, on_delete = models.CASCADE, related_name='publicacao')
#     comentario = models.TextField()
#     data = models.DateTimeField(null=True , auto_now_add=True)
#     foto = models.FileField(null = True, blank = True,  upload_to="static/img")

#     class Meta:
#         verbose_name = 'Comentário'
#         verbose_name_plural = 'Comentários'

#     def __str__(self):
#         return self.usuario.first_name