# Generated by Django 4.1.2 on 2022-11-04 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_search'),
    ]

    operations = [
        migrations.DeleteModel(
            name='search',
        ),
    ]