# Generated by Django 3.1.2 on 2021-12-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario', '0009_remove_categoria_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100), unique=True),
        ),
    ]
