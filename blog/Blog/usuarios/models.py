from django.contrib.auth.models import User
from django.db import models


class ocupacao(models.Model):
    OCUPACAO_CHOICES = [
        ('e', 'Estudante'), ('t', 'Trabalha na área')
        ]


class Linguagens(models.Model):
    LINGUAGENS_CHOICES = [
        ('p', 'Python'), ('h', 'Html'), ('c', 'Css'), ('js', 'JavaScript'), ('d', 'Django'), ('j', 'Java'),
        ]

class usuarios(models.Model):
    nome = models.CharField(max_length=150)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_lenght=50)
    endereco = models.CharField(max_lenght=150)
    aniversario = models.DataField()
    ocupacao = models.CharField(max_length=20, choices= OCUPACAO_CHOICES, default='Estudante')
    linguagens = models.CharField(max_length=20, choices= LINGUAGENS_CHOICES, default='Python')
