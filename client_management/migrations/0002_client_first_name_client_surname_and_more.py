# Generated by Django 4.1.7 on 2023-03-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='client',
            name='surname',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='relationshipmanager',
            name='first_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='relationshipmanager',
            name='surname',
            field=models.CharField(default=None, max_length=200),
        ),
    ]