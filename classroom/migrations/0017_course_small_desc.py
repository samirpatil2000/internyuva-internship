# Generated by Django 3.1.5 on 2021-03-24 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0016_category_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='small_desc',
            field=models.CharField(blank=True, help_text='Add small descriptions over here', max_length=500, null=True),
        ),
    ]