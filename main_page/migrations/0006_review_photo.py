# Generated by Django 5.1 on 2024-09-01 16:08

import main_page.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(default='', upload_to=main_page.models.Review.get_file_name),
        ),
    ]
