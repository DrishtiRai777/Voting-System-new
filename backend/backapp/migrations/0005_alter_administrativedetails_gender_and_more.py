# Generated by Django 5.1.4 on 2025-03-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0004_alter_administrativedetails_institution_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedetails',
            name='gender',
            field=models.CharField(blank=True, db_column='Gender', max_length=100),
        ),
        migrations.AlterField(
            model_name='usersdetail',
            name='gender',
            field=models.CharField(blank=True, db_column='Gender', max_length=100),
        ),
    ]
