# Generated by Django 5.0.2 on 2024-03-12 20:01

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0010_alter_triage_value_of_the_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='hearing_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='triage',
            name='procedural_stage',
            field=models.CharField(choices=[('INGRESSADOS', 'Joined'), ('AVULSO', 'Loose')], default='INGGRESSADOS'),
        ),
        migrations.AlterField(
            model_name='ceara',
            name='cpf_cnpj',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(code='invalid_cpf_cnpj', message='O CPF ou CNPJ deve estar no formato correto.', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$|^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')]),
        ),
        migrations.AlterField(
            model_name='riodejaneiro',
            name='cpf_cnpj',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(code='invalid_cpf_cnpj', message='O CPF ou CNPJ deve estar no formato correto.', regex='^\\d{3}\\.\\d{3}\\.\\d{3}-\\d{2}$|^\\d{2}\\.\\d{3}\\.\\d{3}/\\d{4}-\\d{2}$')]),
        ),
        migrations.AlterField(
            model_name='triage',
            name='number_of_process',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_number_of_process', message='O número do processo deve estar no formato ^\\d{7}-\\d{2}\\.\\d{4}\\.\\d\\.\\d{2}\\.\\d{4}$', regex='^\\d{7}-\\d{2}\\.\\d{4}\\.\\d\\.\\d{2}\\.\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='triage',
            name='obligation_to_do',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
