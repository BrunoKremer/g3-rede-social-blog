# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.db import models

# class UsuarioManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError('O e-mail é obrigatório')
#         email = self.normalize_email(email)
#         user = self.model(email=email, username=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password = None, **extra_fields):
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
   
# class Usuarios(AbstractUser):
#     email = models.EmailField(max_length=254, unique=True)
#     telefone = models.CharField(max_length=15)
#     endereco = models.CharField(max_length=150)
#     aniversario = models.DateField()
#     OCUPACAO_CHOICES = [
#         ('e', 'Estudante'), ('t', 'Trabalha na área')
#         ]
#     LINGUAGENS_CHOICES = [
#         ('p', 'Python'), ('h', 'Html'), ('c', 'Css'), ('js', 'JavaScript'), ('d', 'Django'), ('j', 'Java'),
#         ]

#     ocupacao = models.CharField(max_length=20, choices= OCUPACAO_CHOICES, default='Estudante')
#     linguagens = models.CharField(max_length=20, choices= LINGUAGENS_CHOICES, default='Python')

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'telefone', 'aniversario','endereco', 'ocupacao', 'linguagens'] 

#     def __str__ (self):
#         return self.email

#     objects = UsuarioManager

