# Generated by Django 3.1.5 on 2021-01-29 14:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dprocess', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassType',
            new_name='BusinessType',
        ),
    ]
