# Generated by Django 3.2.6 on 2021-09-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_remove_indicacao_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicacao',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]