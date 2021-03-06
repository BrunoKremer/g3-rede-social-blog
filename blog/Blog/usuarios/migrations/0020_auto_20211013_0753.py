# Generated by Django 3.2.6 on 2021-10-13 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0019_auto_20211012_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='seguindo',
        ),
        migrations.AlterField(
            model_name='seguir',
            name='seguidores',
            field=models.ManyToManyField(related_name='seguidores', to='usuarios.CustomUser'),
        ),
        migrations.AlterField(
            model_name='seguir',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seguidor', to='usuarios.customuser'),
        ),
    ]
