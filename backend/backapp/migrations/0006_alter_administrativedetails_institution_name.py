# Generated by Django 5.1.4 on 2025-03-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0005_alter_administrativedetails_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativedetails',
            name='institution_name',
            field=models.CharField(db_column='Instituition Name', max_length=255),
        ),
    ]
