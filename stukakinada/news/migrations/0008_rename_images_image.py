# Generated by Django 4.1.2 on 2022-11-04 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_images_delete_attachment_remove_newsarticle_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='images',
            new_name='image',
        ),
    ]
