# Generated by Django 3.2.6 on 2021-10-13 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-criacao'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentários'},
        ),
        migrations.AlterModelOptions(
            name='publicacao',
            options={'ordering': ['-data'], 'verbose_name': 'Publicação', 'verbose_name_plural': 'Publicações'},
        ),
    ]
