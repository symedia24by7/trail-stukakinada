# Generated by Django 4.1.2 on 2022-11-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_rename_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
