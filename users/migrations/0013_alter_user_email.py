# Generated by Django 5.0.2 on 2024-03-16 00:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='O e-mail deve estar no formato nome.sobrenome@meirelesefreitas.adv.br', regex=' ?(\\w+\\.\\w+@meirelesefreitas(?:\\.adv\\.br)+)')]),
        ),
    ]
