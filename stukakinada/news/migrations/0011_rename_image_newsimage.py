# Generated by Django 4.1.2 on 2022-11-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_delete_search'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='image',
            new_name='newsImage',
        ),
    ]
