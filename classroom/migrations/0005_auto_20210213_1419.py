# Generated by Django 3.1.5 on 2021-02-13 14:19

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('classroom', '0004_auto_20210213_1416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Note',
            new_name='Notes',
        ),
    ]
