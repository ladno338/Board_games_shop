# Generated by Django 5.0.1 on 2024-01-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deployer',
            new_name='Publisher',
        ),
    ]
