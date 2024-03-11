# Generated by Django 5.0.2 on 2024-03-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0007_alter_ceara_cpf_cnpj_alter_riodejaneiro_cpf_cnpj_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triage',
            name='fatal_deadline',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='hearing_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='value_of_the_fine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
