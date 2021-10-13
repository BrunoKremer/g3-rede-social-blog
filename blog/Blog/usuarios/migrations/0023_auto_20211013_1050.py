# Generated by Django 3.2.6 on 2021-10-13 13:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0022_alter_seguir_seguidores'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='seguidores',
            field=models.ManyToManyField(related_name='seguidores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Seguir',
        ),
    ]
