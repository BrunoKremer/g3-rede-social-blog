# Generated by Django 3.2.4 on 2021-08-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210830_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]