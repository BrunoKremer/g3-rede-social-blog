# Generated by Django 3.2.6 on 2021-10-07 17:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20211006_1729'),
        ('social', '0016_alter_publicacao_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comentario', models.TextField(blank=True, null=True)),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('publicacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.publicacao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.customuser')),
            ],
        ),
    ]
