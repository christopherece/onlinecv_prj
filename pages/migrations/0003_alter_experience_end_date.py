# Generated by Django 5.1.7 on 2025-03-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
