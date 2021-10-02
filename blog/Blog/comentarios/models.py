from django.db import models
from social.models import Publicacao
from usuarios.models import CustomUser
# Create your models here.
# Model de comentario na rede social
class Comentario(models.Model):
    usuario=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True, related_name='usuario_social')
    email =models.CharField(max_length=255, null=True)
    publicacao = models.ForeignKey(Publicacao, on_delete = models.CASCADE, related_name='publicacao')
    comentario = models.TextField()
    data = models.DateTimeField(null=True , auto_now_add=True)
    foto = models.FileField(null = True, blank = True,  upload_to="static/img")

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.usuario.first_name