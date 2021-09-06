from django.contrib.auth.models import User
from django.db import models


class Usuario(models.Model):
    CATEGORIA_CHOICES = [
        ('p', 'Python'), ('h', 'Html'), ('c', 'Css'), ('js', 'JavaScript'), ('d', 'Django'), ('j', 'Java'), ('a', 'Api'), ('g', 'Geral')
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=10, choices= CATEGORIA_CHOICES, default='Python')
    

    def __str__(self):
        return self.usuario