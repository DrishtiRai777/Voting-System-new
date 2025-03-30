# Generated by Django 5.1.4 on 2025-03-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0002_alter_administrativedetails_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrativedetails',
            name='email_address_of_seceretary',
        ),
        migrations.RemoveField(
            model_name='administrativedetails',
            name='seceretary_name',
        ),
        migrations.AddField(
            model_name='administrativedetails',
            name='email_address_of_secretary',
            field=models.CharField(blank=True, db_column='Email Address Of Secretary', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='administrativedetails',
            name='secretary_name',
            field=models.CharField(blank=True, db_column='Secretary Name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='contact_number',
            field=models.CharField(blank=True, db_column='Contact Number', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='contact_number_of_member_2',
            field=models.CharField(blank=True, db_column='Contact Number of Member 2', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='email_address_of_member_2',
            field=models.CharField(blank=True, db_column='Email Address of Member 2', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='name_of_admin',
            field=models.CharField(blank=True, db_column='Name of Admin', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='password',
            field=models.CharField(blank=True, db_column='Password', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='team_member_1_name',
            field=models.CharField(blank=True, db_column='Team Member 1 Name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='team_member_2_name',
            field=models.CharField(blank=True, db_column='Team Member 2 Name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='administrativedetails',
            name='username',
            field=models.CharField(blank=True, db_column='Username', max_length=255, null=True),
        ),
    ]
