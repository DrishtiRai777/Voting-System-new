# Generated by Django 5.1.4 on 2025-03-17 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedetails',
            name='date_of_birth',
            field=models.DateField(blank=True, db_column='Date of Birth', null=True),
        ),
    ]
