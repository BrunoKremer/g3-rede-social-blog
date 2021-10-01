from django.contrib.auth.models import User
from django.db import models
from usuarios.models import CustomUser

# Modelo de Publicação
# Estamos importando o Custom User para autenticar o usuário
class Publicacao(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add= True)
    foto = models.FileField(null = True, blank = True,  upload_to="static/img/")
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