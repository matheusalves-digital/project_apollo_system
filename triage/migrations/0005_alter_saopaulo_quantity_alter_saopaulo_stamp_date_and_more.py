# Generated by Django 5.0.2 on 2024-03-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0004_alter_triage_preliminary_situation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saopaulo',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='saopaulo',
            name='stamp_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='saopaulo',
            name='value_of_the_claim',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='fatal_deadline',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='hearing_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='judicial_determination',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='type_of_fine',
            field=models.CharField(choices=[('DIÁRIA', 'Daily'), ('ÚNICA', 'Only'), ('POR HORA', 'Hours'), ('POR ATOS', 'By Acts')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='triage',
            name='value_of_the_fine',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
