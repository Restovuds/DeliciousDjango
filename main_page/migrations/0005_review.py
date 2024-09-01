# Generated by Django 5.1 on 2024-09-01 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_chef_chefsocial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('worked_at', models.CharField(max_length=50)),
                ('rating', models.SmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('text', models.TextField(max_length=500)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ('position',),
            },
        ),
    ]
