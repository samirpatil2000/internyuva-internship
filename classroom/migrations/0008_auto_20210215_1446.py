# Generated by Django 3.1.5 on 2021-02-15 14:46

import classroom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_merge_20210215_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(default=classroom.models.generate_random_string, max_length=20),
        ),
    ]