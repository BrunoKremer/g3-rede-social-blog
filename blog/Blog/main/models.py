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
    photo = models.FileField(null=True, blank=True, upload_to="static/img/produtos")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.title