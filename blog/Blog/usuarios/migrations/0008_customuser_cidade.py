# Generated by Django 3.2.6 on 2021-09-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_customuser_cep'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cidade',
            field=models.CharField(max_length=155, null=True),
        ),
    ]
