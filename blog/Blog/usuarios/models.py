# from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.fields import CharField
from localflavor.br.models import BRStateField, BRPostalCodeField
from django.contrib.auth.models import User

# Model de usuário
# BRStateField e BRPostalCodeField são importações de uma biblioteca chamada localFlavor para UF e CEP

class CustomUser(User):
    telefone = models.CharField(max_length=15, null=True, blank=True)
    aniversario = models.DateField(auto_now_add=False, null=True, blank=True)
    foto = models.ImageField(null=True, blank=True, upload_to="static/img/", default="static/img/default_profile_image.jpg")
    estado = BRStateField(null = True, blank = True)
    CEP = BRPostalCodeField(null = True)
    cidade = models.CharField(max_length=155, null=True)
    genero_choices = [("F", "Feminino"), ("H", "Masculino"), ("O", "Outro")]
    genero = models.CharField(choices=genero_choices, default="M", max_length=1)
    link_fb = models.CharField(null=True, blank=True, max_length=255)
    link_git = models.CharField(null=True, blank=True, max_length=255)
    link_tt = models.CharField(null=True, blank=True, max_length=255)
    link_ig = models.CharField(null=True, blank=True, max_length=255)
    # seguidores = models.ManyToManyField(User,blank=True,related_name='Seguidores')
    ocupacao_choices = [
        ('e', 'Estudante'), ('t', 'Trabalha na área')
        ]
    ocupacao = models.CharField(max_length=20, choices= ocupacao_choices, default='Estudante')
    

    def __str__(self):
        return self.first_name




class Seguir(models.Model):
    user = models.OneToOneField(CustomUser,null=True ,blank=True,related_name='seguido',on_delete=models.CASCADE)
    seguidores = models.ManyToManyField(CustomUser, related_name='seguidor')

