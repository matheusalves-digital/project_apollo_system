# Generated by Django 5.0.2 on 2024-03-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0012_alter_triage_hearing_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triage',
            name='hearing_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]