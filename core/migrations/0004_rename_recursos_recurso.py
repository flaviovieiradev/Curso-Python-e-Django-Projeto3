# Generated by Django 5.0.7 on 2024-08-05 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_recursos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recursos',
            new_name='Recurso',
        ),
    ]