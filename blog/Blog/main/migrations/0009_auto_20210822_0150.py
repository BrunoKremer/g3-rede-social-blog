# Generated by Django 3.2.6 on 2021-08-22 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210820_1629'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='category',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='indicacao',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='indicacao',
            old_name='category',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='indicacao',
            old_name='created_in',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='indicacao',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='conteúdo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_in',
            new_name='criado_em',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_by',
            new_name='criado_por',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='photo',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
    ]
