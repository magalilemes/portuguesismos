# Generated by Django 3.1.2 on 2021-12-23 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dicionario', '0008_auto_20211223_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
    ]